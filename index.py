from pyscript import when
from ultralytics import hub, YOLO
from autodistill_grounded_sam import GroundedSAM
from autodistill.detection import CaptionOntology

@when("click", "button")
def hello():
    print("hello")

print(hub.login("86d48192211ece7b9fa5e0ff811f82e378538ca65c"))