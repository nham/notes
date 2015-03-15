import os, subprocess

def ensure_dir(f):
    d = os.path.dirname(f)
    if len(d) == 0:
        d = "./"
    if not os.path.exists(d):
        os.makedirs(d)

class Generator:
    def __init__(self, output_path="_schol_output/",
                 default_page_before_body=None,
                 default_page_after_body=None,
                 default_css_files=[]):
        self.output_path = output_path

        self.default_page_before_body = default_page_before_body
        self.default_page_after_body = default_page_after_body
        self.default_css_files = default_css_files


    def copy_file(self, in_path, filename, out_path=None):
        if out_path is None:
            out_path = in_path

        in_file = in_path + filename
        out_file = self.output_path + out_path + filename
        ensure_dir(out_file)
        subprocess.call(['cp', in_file, out_file])


    def gen_page_file(self, input_file, path_rel_to_output,
                        css_files=None,
                        page_before_body=None,
                        page_after_body=None):


        # TODO: figure out whether to use path joining here instead
        # and change output_path => output_folder
        output_file_path = self.output_path + path_rel_to_output

        ensure_dir(output_file_path)

        scholdoc_call = (['scholdoc', input_file,
                      '-f', 'markdown_scholarly',
                      '-t', 'html5',
                      '-o', output_file_path,
                      '--smart'])

        if css_files is None:
            css_files = self.default_css_files

        for file_name in css_files:
            scholdoc_call += ['--css', file_name]


        if page_before_body is None:
            page_before_body = self.default_page_before_body

        if page_before_body is not None:
            pass
            #pandoc_call += ['--include-before-body', page_before_body]

        p = subprocess.call(scholdoc_call)


def gen_notes(gen):
    folder_name = 'schol_notes/'

    for i, fname in enumerate( os.listdir(folder_name) ):
        if fname.endswith('.md'):
            fname_html = fname.replace('.md', '.html')
            fpath = folder_name + fname
            out_fpath = '/' + fname_html
            gen.gen_page_file(fpath, out_fpath)

        else:
            # assume it's something that needs to be copied to output
            # folder (like an image)
            gen.copy_file(folder_name, fname, '/')


gen = Generator(default_css_files=['/schol_css/style.css'])

gen_notes(gen)
gen.copy_file('schol_css/', 'style.css')
