def union other_df
      index = (@index.to_a + other_df.index.to_a).uniq
      df = row[*(@index.to_a - other_df.index.to_a)]

      df = df.concat(other_df)
      df.index = Daru::Index.new(index)
      df
    end