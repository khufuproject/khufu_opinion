from paste.script.templates import Template
from paste.util.template import paste_script_template_renderer


class KhufuOpinionProjectTemplate(Template):
    _template_dir = 'paster_template'
    summary = 'khufu_opinion starter project'
    template_renderer = staticmethod(paste_script_template_renderer)
