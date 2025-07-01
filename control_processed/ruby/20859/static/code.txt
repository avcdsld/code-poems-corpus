def to_dot_graph (params = {})
      params['name'] ||= self.class.name.gsub(/:/,'_')
      fontsize   = params['fontsize'] || '8'
      fontname   = params['fontname'] || 'Times-Roman'
      graph      = (directed? ? DOT::Digraph : DOT::Subgraph).new(params)
      edge_class = directed? ? DOT::DirectedEdge : DOT::Edge
      shape = params['shape'] || 'ellipse'
      each_vertex do |v|
        name = v.to_s
        graph << DOT::Node.new('name'     => name,
                               'fontsize' => fontsize,
                               'label'    => name,
                               'shape'    => shape,
                               'fontname' => fontname)
      end
      each_edge do |u,v|
        if respond_to?(:is_abnormal?)
          if is_abnormal?(u, v) && is_block_taken?(u, v)
            color = 'blue'
          elsif is_abnormal?(u, v)
            color = 'red'
          elsif is_fake?(u, v)
            color = '#bbbbbb'
          else
            color = 'black'
          end
          style = (is_fake?(u, v) || !is_executable?(u, v)) ? 'dashed' : 'solid'
        else
          color = 'black'
          style = 'solid'
        end
        graph << edge_class.new('from'     => u.to_s,
                                'to'       => v.to_s,
                                'fontsize' => fontsize,
                                'fontname' => fontname,
                                'color'    => color,
                                'style'    => style)
      end
      graph
    end