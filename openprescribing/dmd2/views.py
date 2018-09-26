from django.core.exceptions import ObjectDoesNotExist
from django.db.models import ForeignKey
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import VMP, VMPP, AMP, AMPP

import json

obj_type_to_cls = {
    "vmp": VMP,
    "vmpp": VMPP,
    "amp": AMP,
    "ampp": AMPP,
}


def _build_row(obj, field):
    value = getattr(obj, field.name)
    if value is None:
        return

    if isinstance(field, ForeignKey):
        try:
            value = value.descr
        except AttributeError:
            value = value.nm

    return {"key": field.help_text, "value": value}


def dmd_obj_view(request, obj_type, id):
    try:
        cls = obj_type_to_cls[obj_type]
    except KeyError:
        raise Http404

    obj = get_object_or_404(cls, id=id)

    # I'm loading this from a JSON file on each request because this is quicker
    # than keeping the data in Python and waiting for the server to reload on
    # each change.  TODO change this once the we've worked out what fields to
    # show, and in what order.
    with open("dmd2/gen_models/view-schema.json") as f:
        schema = json.load(f)

    fields_by_name = {field.name: field for field in cls._meta.fields}
    rels_by_name = {rel.name: rel for rel in cls._meta.related_objects}

    rows = []

    # Fields for the object
    for field_name in schema[obj_type]["fields"]:
        field = fields_by_name[field_name]

        row = _build_row(obj, field)
        if row is not None:
            rows.append(row)

    # Related objects (eg VPIs for a VMP)
    for rel_name in schema[obj_type]["other_relations"]:
        relname = rel_name.replace("_", "")
        rel = rels_by_name[relname]
        model = rel.related_model
        rel_fields_by_name = {field.name: field for field in model._meta.fields}

        if rel.multiple:
            related_instances = getattr(obj, rel.get_accessor_name()).all()
            if not related_instances.exists():
                continue
        else:
            try:
                related_instances = [getattr(obj, rel.name)]
            except ObjectDoesNotExist:
                continue

        for related_instance in related_instances:
            rows.append({"title": model._meta.verbose_name})
            for field_name in schema[rel_name]["fields"]:
                if field_name == obj_type:
                    continue
                field = rel_fields_by_name[field_name]
                row = _build_row(related_instance, field)
                if row is not None:
                    rows.append(row)

    # Related dm+d objects (for a VMP, these will be VMPPs and AMPs)
    for rel_name in schema[obj_type]["dmd_obj_relations"]:
        relname = rel_name.replace("_", "")
        rel = rels_by_name[relname]
        assert rel.multiple
        model = rel.related_model

        related_instances = getattr(obj, rel.get_accessor_name()).all()
        if not related_instances.exists():
            continue

        rows.append({"title": model._meta.verbose_name_plural})
        for related_instance in related_instances:
            try:
                value = related_instance.descr
            except AttributeError:
                value = related_instance.nm
            link = reverse("dmd_obj", args=[rel_name, related_instance.id])
            rows.append({"key": related_instance.id, "value": value, "link": link})

    ctx = {
        "title": "{} {}".format(cls.__name__, id),
        "rows": rows,
    }
    return render(request, "dmd/dmd_obj.html", ctx)
