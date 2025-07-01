def to_local_paths( notations )
      if Naether.platform == 'java'
        Naether::Java.convert_to_ruby_array(
            Naether::Java.exec_static_method(
                'com.tobedevoured.naether.util.Notation',
                'getLocalPaths',
                [local_repo_path, notations ],
                ['java.lang.String', 'java.util.List'] ) )
      else
        paths =  Naether::Java.exec_static_method(
            'com.tobedevoured.naether.util.Notation',
            'getLocalPaths',
            [local_repo_path, Naether::Java.convert_to_java_list(notations) ],
            ['java.lang.String', 'java.util.List'] )
        Naether::Java.convert_to_ruby_array( paths, true )
      end

    end