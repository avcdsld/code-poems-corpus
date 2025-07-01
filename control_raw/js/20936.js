function JaroWinklerDistance(s1, s2, dj, ignoreCase) {
    if (s1 === s2) {
        return 1;
    } else {
        if (ignoreCase) {
          s1 = s1.toLowerCase();
          s2 = s2.toLowerCase();
        }

        //console.log(news1);
        //console.log(news2);

        var jaro = (typeof(dj) === 'undefined') ? distance(s1, s2) : dj;
        var p = 0.1; // default scaling factor
        var l = 0 // length of the matching prefix
        while(s1[l] === s2[l] && l < 4) {
            l++;
        }

        // HtD: 1 - jaro >= 0
        return jaro + l * p * (1 - jaro);
    }
}