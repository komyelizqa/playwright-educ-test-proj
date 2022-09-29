class TestPageDom:

    def test_table(self, dom_page):
        dom_page.navigate_to('Challenging DOM')
        dom_page.check_dom_page_opened()
        dom_page.check_table_cell('Iuvaret0')
        dom_page.check_table_cell('Definiebas3')
        dom_page.check_table_cell('Phaedrum9')

    def test_button(self, dom_page):
        dom_page.navigate_to('Challenging DOM')
        assert dom_page.button_is_clickable()


