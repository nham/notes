import os, subprocess

def ensure_dir(f):
    d = os.path.dirname(f)
    if len(d) == 0:
        d = "./"
    if not os.path.exists(d):
        os.makedirs(d)

class Generator:
    def __init__(self, output_path="_output/",
                 default_page_before_body=None,
                 default_page_after_body=None,
                 default_css_files=[]):
        self.output_path = output_path

        self.default_page_before_body = default_page_before_body
        self.default_page_after_body = default_page_after_body
        self.default_css_files = default_css_files


    def copy_file(self, folder, filename):
        in_file = folder + filename
        out_file = self.output_path + in_file
        ensure_dir(out_file)
        subprocess.call(['cp', in_file, out_file])


    # title is actually configured in page_markdown.
    def gen_page_string(self, page_markdown, path_rel_to_output,
                        css_files=None,
                        is_mathjax_on=False,
                        page_before_body=None,
                        page_after_body=None):

        # TODO: figure out whether to use path joining here instead
        # and change output_path => output_folder
        output_file_path = self.output_path + path_rel_to_output

        ensure_dir(output_file_path)

        pandoc_call = (['pandoc', '--standalone',
                      '-f', 'markdown_phpextra+yaml_metadata_block+simple_tables',
                      '-t', 'html5',
                      '-o', output_file_path,
                      '--smart'])

        if is_mathjax_on:
            pandoc_call += ['--mathjax']


        if css_files is None:
            css_files = self.default_css_files

        for file_name in css_files:
            pandoc_call += ['--css', file_name]


        if page_before_body is None:
            page_before_body = self.default_page_before_body

        if page_before_body is not None:
            pandoc_call += ['--include-before-body', page_before_body]


        if page_after_body is None:
            page_after_body = self.default_page_after_body

        if page_after_body is not None:
            pandoc_call += ['--include-after-body', page_after_body]


        p = subprocess.Popen(pandoc_call, stdin=subprocess.PIPE)
        p.communicate(input=bytes(page_markdown, 'utf-8'))


    # input is a file name instead of markdown string
    def gen_page_file(self, input_file, path_rel_to_output,
                        css_files=None,
                        is_mathjax_on=False,
                        page_before_body=None,
                        page_after_body=None):


        # TODO: figure out whether to use path joining here instead
        # and change output_path => output_folder
        output_file_path = self.output_path + path_rel_to_output

        ensure_dir(output_file_path)

        pandoc_call = (['pandoc', input_file,
                      '--standalone',
                      '-t', 'html5',
                      '-o', output_file_path,
                      '--smart'])

        if is_mathjax_on:
            pandoc_call += ['--mathjax']


        if css_files is None:
            css_files = self.default_css_files

        for file_name in css_files:
            pandoc_call += ['--css', file_name]


        if page_before_body is None:
            page_before_body = self.default_page_before_body

        if page_before_body is not None:
            pandoc_call += ['--include-before-body', page_before_body]


        if page_after_body is None:
            page_after_body = self.default_page_after_body

        if page_after_body is not None:
            pandoc_call += ['--include-after-body', page_after_body]


        p = subprocess.call(pandoc_call)



# first concern is the exact organization of
# notes. if each note is a unit of review, it seems like they
# should be fairly small.

def gen_notes(gen):
    list_md = ""
    folder_name = 'notes/'

    for i, fname in enumerate( os.listdir(folder_name) ):
        if fname.endswith('.md'):
            fname_html = fname.replace('.md', '.html')

            list_md += " - [{}]({})\n".format(
                    fname.replace('.md', ''),
                    fname_html
                  )

            fpath = folder_name + fname
            out_fpath = '/' + fname_html
            gen.gen_page_file(fpath, out_fpath,
                              is_mathjax_on=True)

        else:
            # assume it's something that needs to be copied to output
            # folder (like an image)
            # TODO: I think this has a problem. need to check
            gen.copy_file(folder_name, fname)



    notes_md = """---
title: notes
---
<div id="titlenav"><span id="title">notes</span></div>

{}
""".format(list_md)

    # generate notes index
    gen.gen_page_string(notes_md, 'index.html')



gen = Generator(default_css_files=['/css/style.css'],
                default_page_before_body='includes/before_body.html',
                default_page_after_body='includes/after_body.html')

gen_notes(gen)
gen.copy_file('css/', 'style.css')
