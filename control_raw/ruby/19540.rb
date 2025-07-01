def position_object(col_start, row_start, x1, y1, width, height)   #:nodoc:
    # col_start;  # Col containing upper left corner of object
    # x1;         # Distance to left side of object

    # row_start;  # Row containing top left corner of object
    # y1;         # Distance to top of object

    # col_end;    # Col containing lower right corner of object
    # x2;         # Distance to right side of object

    # row_end;    # Row containing bottom right corner of object
    # y2;         # Distance to bottom of object

    # width;      # Width of image frame
    # height;     # Height of image frame

    # Adjust start column for offsets that are greater than the col width
    x1, col_start = adjust_col_position(x1, col_start)

    # Adjust start row for offsets that are greater than the row height
    y1, row_start = adjust_row_position(y1, row_start)

    # Initialise end cell to the same as the start cell
    col_end    = col_start
    row_end    = row_start

    width     += x1
    height    += y1

    # Subtract the underlying cell widths to find the end cell of the image
    width, col_end = adjust_col_position(width, col_end)

    # Subtract the underlying cell heights to find the end cell of the image
    height, row_end = adjust_row_position(height, row_end)

    # Bitmap isn't allowed to start or finish in a hidden cell, i.e. a cell
    # with zero eight or width.
    #
    return if size_col(col_start) == 0
    return if size_col(col_end)   == 0
    return if size_row(row_start) == 0
    return if size_row(row_end)   == 0

    # Convert the pixel values to the percentage value expected by Excel
    x1 = 1024.0 * x1     / size_col(col_start)
    y1 =  256.0 * y1     / size_row(row_start)
    x2 = 1024.0 * width  / size_col(col_end)
    y2 =  256.0 * height / size_row(row_end)

    # Simulate ceil() without calling POSIX::ceil().
    x1 = (x1 +0.5).to_i
    y1 = (y1 +0.5).to_i
    x2 = (x2 +0.5).to_i
    y2 = (y2 +0.5).to_i

    [
      col_start, x1,
      row_start, y1,
      col_end,   x2,
      row_end,   y2
    ]
  end