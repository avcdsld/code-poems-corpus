def get_frames(root_path):
   """Get path to all the frame in view SAX and contain complete frames"""
   ret = []
   for root, _, files in os.walk(root_path):
       root=root.replace('\\','/')
       files=[s for s in files if ".dcm" in s]
       if len(files) == 0 or not files[0].endswith(".dcm") or root.find("sax") == -1:
           continue
       prefix = files[0].rsplit('-', 1)[0]
       fileset = set(files)
       expected = ["%s-%04d.dcm" % (prefix, i + 1) for i in range(30)]
       if all(x in fileset for x in expected):
           ret.append([root + "/" + x for x in expected])
   # sort for reproduciblity
   return sorted(ret, key = lambda x: x[0])