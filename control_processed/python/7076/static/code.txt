def get_header_guard_dmlc(filename):
    """Get Header Guard Convention for DMLC Projects.
    For headers in include, directly use the path
    For headers in src, use project name plus path
    Examples: with project-name = dmlc
        include/dmlc/timer.h -> DMLC_TIMTER_H_
        src/io/libsvm_parser.h -> DMLC_IO_LIBSVM_PARSER_H_
    """
    fileinfo = cpplint.FileInfo(filename)
    file_path_from_root = fileinfo.RepositoryName()
    inc_list = ['include', 'api', 'wrapper']

    if file_path_from_root.find('src/') != -1 and _HELPER.project_name is not None:
        idx = file_path_from_root.find('src/')
        file_path_from_root = _HELPER.project_name +  file_path_from_root[idx + 3:]
    else:
        for spath in inc_list:
            prefix = spath + os.sep
            if file_path_from_root.startswith(prefix):
                file_path_from_root = re.sub('^' + prefix, '', file_path_from_root)
                break
    return re.sub(r'[-./\s]', '_', file_path_from_root).upper() + '_'