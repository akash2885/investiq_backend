from .schema import Politician, PoliticianSchema, PoliticianCreateSchema
from ninja import NinjaAPI


api = NinjaAPI()


@api.get("politician/", response=list[PoliticianSchema])
def get_politician(request):
    politician = Politician.objects.all()
    return politician


@api.get("politician/{p_id}", response=PoliticianSchema)
def get_one_politician(request, p_id : int):
    politician = Politician.objects.filter(id = p_id).get()
    return politician


@api.post("politician/", response=PoliticianCreateSchema)
def post_politician(request, data : PoliticianCreateSchema):
    new_politician = Politician.objects.create(**data.dict())
    return new_politician


@api.put("politician/{p_id}", response=PoliticianCreateSchema)
def put_politician(request, data : PoliticianCreateSchema, p_id : int):
    updated_politician = Politician.objects.filter(id = p_id).update(**data.dict())
    if updated_politician:
        return Politician.objects.get(id = p_id)


@api.delete("politician/{p_id}")
def delete_politician(request, p_id : int):
    deleted_politician = Politician.objects.filter(id = p_id).delete()
    if deleted_politician:
        return {"message" : "deleted politician"}