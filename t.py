# from gingerit.gingerit import GingerIt
# text = 'Hence it is that is almost a definition of a gentleman to say he is one who never inflicts pain. This description is both refined '
# parser = GingerIt()
# correct_text = parser.parse(text)
# print(correct_text)



from gramformer import Gramformer


gf = Gramformer(models=3, use_gpu=False)