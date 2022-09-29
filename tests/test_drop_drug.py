class TestDrugDrop:

    def test_drug_drop_page(self, drug_drop):
        drug_drop.navigate_to('Drag and Drop')
        drug_drop.drug_and_drop()
        drug_drop.check_elements_after_dropping()

