function(n) {
      var i = n,
          j = 0,
          temp;
      var array = [];
      for(var q=0;q<n;q++)array[q]=q;
      while (i--) {
          j = Math.floor(Math.random() * (i+1));
          temp = array[i];
          array[i] = array[j];
          array[j] = temp;
      }
      return array;
    }