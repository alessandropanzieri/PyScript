from pyscript import when
from autodistill_grounded_sam import GroundedSAM
from autodistill.detection import CaptionOntology

@when("click", "button")
def hello():
    print("hello")