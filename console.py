import pdb
from models.vet import Vet
from models.animal import Animal

import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository

pdb.set_trace()
# vet_repository.delete_all()
# animal_repository.delete_all()

# vet_1 = Vet("Dr Ink", "More likely to anaesthetise themselves before the animal")
# vet_repository.add_vet(vet_1)

# vet_repository.select_all()

# animal_1 = Animal("Barney", "Dinosaur", "+447471234581", "12APR1992", "prosthetic tail insertion", vet_1)
# animal_repository.add_animal(animal_1)


animal_repository.select_all()


# vet_repository.delete(vet_1.id)

# vet_repository.select_all()
