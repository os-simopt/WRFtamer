import panel as pn

from src.gui.proj_tab import proj_tab
from src.gui.exp_tab import exp_tab
from src.gui.about_tab import about_tab
from src.gui.wrfplotter_tab import wrfplotter_tab

pn.extension("tabulator")
tabulator_formatters = {"select": {"type": "tickCross"}}


class GUI:
    def __init__(self):
        self.project = proj_tab()
        self.experiment = exp_tab(self.project.mc_proj)
        self.about = about_tab()
        self.wp = wrfplotter_tab()

    def view(self):
        all_tabs = pn.Tabs(
            self.project.view(),
            self.experiment.view(),
            self.wp.view(),
            self.about.view()
        )

        return all_tabs


a = GUI()
a.view().servable("WRFtamer")

# TODO (for Next Version):
# - add etalevel program
# - add domänenübersicht.