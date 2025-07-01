def diff_args(user_args = [])
      upstream_item = upstream_item_for_revision(base_revision)

      # We do not need to spend the time to copy the content outside the
      # mirror from HEAD because --relative will exclude it anyway.  Rename
      # detection seems to apply only to the files included in the diff, so we
      # shouldn't have another bug like
      # https://github.com/cristibalan/braid/issues/41.
      base_tree = git.make_tree_with_item(nil, path, upstream_item)

      # Note: --relative does a naive prefix comparison.  If we set (for
      # example) `--relative=a/b`, that will match an unrelated file or
      # directory name `a/bb`.  If the mirror is a directory, we can avoid this
      # by adding a trailing slash to the prefix.
      #
      # If the mirror is a file, the only way we can avoid matching a path like
      # `a/bb` is to pass a path argument to limit the diff.  This means if the
      # user passes additional path arguments, we won't get the behavior we
      # expect, which is the intersection of the user-specified paths with the
      # mirror.  However, it's probably unreasonable for a user to pass path
      # arguments when diffing a single-file mirror, so we ignore the issue.
      #
      # Note: This code doesn't handle various cases in which a directory at the
      # root of a mirror turns into a file or vice versa.  If that happens,
      # hopefully the user takes corrective action manually.
      if upstream_item.is_a?(git.BlobWithMode)
        # For a single-file mirror, we use the upstream basename for the
        # upstream side of the diff and the downstream basename for the
        # downstream side, like what `git diff` does when given two blobs as
        # arguments.  Use --relative to strip away the entire downstream path
        # before we add the basenames.
        return [
          '--relative=' + path,
          '--src-prefix=a/' + File.basename(remote_path),
          '--dst-prefix=b/' + File.basename(path),
          base_tree,
          # user_args may contain options, which must come before paths.
          *user_args,
          path
        ]
      else
        return [
          '--relative=' + path + '/',
          base_tree,
          *user_args
        ]
      end
    end