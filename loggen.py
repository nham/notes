import os, subprocess

def ensure_dir(f):
    d = os.path.dirname(f)
    if len(d) == 0:
        d = "./"
    if not os.path.exists(d):
        os.makedirs(d)


def doodoo(mdstr, get_list):
    # the markdown string mdstr passed in is supposed to have one
    # bracket {} for lists that are generated
    mdstr = mdstr.format( get_list() )
    return mdstr


def get_log_entry_list():
    md = ""
    folder_name = 'log/2015/jan/'

    for i, fname in enumerate( os.listdir(folder_name) ):
        if fname.endswith('.md'):
            md += " - [{}]({})\n".format(
                    folder_name.replace('log/', '')+fname.replace('.md', ''),
                    folder_name+fname.replace('.md', '.html')
                  )
        else:
            # assume it's something that needs to be copied to output
            # folder (like an image)
            # TODO: I think this has a problem. need to check
            copy_file(folder_name, fname)

    return md

# first concern is the exact organization of
# notes. if each note is a unit of review, it seems like they
# should be fairly small.

def get_notes_list():
    md = ""
    folder_name = 'notes/'

    for i, fname in enumerate( os.listdir(folder_name) ):
        if fname.endswith('.md'):
            md += " - [{}]({})\n".format(
                    fname.replace('.md', ''),
                    fname.replace('.md', '.html')
                  )
        else:
            # assume it's something that needs to be copied to output
            # folder (like an image)
            # TODO: I think this has a problem. need to check
            copy_file(folder_name, fname)

    return md

index_md = """---
title: daily log
---
[notes](notes/)

## log entries

{}
"""

notes_md = """---
title: notes
---
[daily log](../)

## notes

{}
"""

print( doodoo(index_md, get_log_entry_list) )
print( doodoo(notes_md, get_notes_list) )
