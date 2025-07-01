function (degrees) {
            var sign,
                temp,
                d,
                m,
                s;

            sign = degrees < 0 ? -1 : 1;
            temp = sign * degrees;
            d = Math.floor(temp);
            temp = (temp - d) * 60;
            m = Math.floor(temp);
            temp = (temp - m) * 60;
            s = Math.round(temp);

            if (s == 60) {
                m++;
                s = 0;
            }
            if (m == 60) {
                d++;
                m = 0;
            }

            return (sign == -1 ? "-" : "") + d + "\u00B0" + " " + m + "\u2019" + " " + s + "\u201D";
        }