from Classes import Sheep as S
from Classes import Field as F


Field = F.Field(500, 500)

S1 = S.Sheep(3, 5, 2, Field)
Field.Sheeps.append(S1)
S2 = S.Sheep(3, 3, 2, Field)
Field.Sheeps.append(S2)
S3 = S.Sheep(3, 7, 2, Field)
Field.Sheeps.append(S3)

S3.PrintAllPositions()



