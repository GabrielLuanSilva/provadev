from mongoengine import connect, Document, StringField, ListField, ReferenceField

client = connect('mapa')


class Bairro(Document):
    nome = StringField(required=True)

    def __str__(self):
        return {
            'id': self.id,
            'nome': self.nome,
        }.__str__()


class Cidade(Document):
    nome = StringField(required=True)
    bairros = ListField(ReferenceField(Bairro))

    def __str__(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'bairros': self.bairros
        }.__str__()


class Estado(Document):
    nome = StringField(required=True)
    cidades = ListField(ReferenceField(Cidade))

    def __str__(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cidades': self.cidades
        }.__str__()


Bairro.objects.delete()
Cidade.objects.delete()
Estado.objects.delete()

bairro1 = Bairro(nome="Agostinho").save()
bairro2 = Bairro(nome="Natal").save()
bairro3 = Bairro(nome="Betânia").save()

cidade1 = Cidade(nome='Noronha', bairros=[bairro1, bairro2]).save(),
cidade2 = Cidade(nome='Diamantina', bairros=[bairro3]).save(),

estado1 = Estado(nome="Paraná", cidades=cidade1).save()
estado2 = Estado(nome="Goiás", cidades=cidade2).save()

print('# BAIRROS #')
bairros = Bairro.objects.all()
for bairro in bairros:
    print(bairro)

print('# CIDADES #')
cidades = Cidade.objects.all()
for cidade in cidades:
    print(cidade)

print('# ESTADOS #')
estados = Estado.objects.all()
for estado in estados:
    print(estado)
