from gixy.formatters.base import BaseFormatter
from gixy.formatters._jinja import load_template


class ConsoleFormatter(BaseFormatter):
    def __init__(self):
        super(ConsoleFormatter, self).__init__()
        self.template = load_template('console.j2')

    def format_reports(self, reports, stats):
        return self.template.render(reports=reports, stats=stats)
