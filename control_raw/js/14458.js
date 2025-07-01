function zOrder(x, y, minX, minY, invSize) {
       // coords are transformed into non-negative 15-bit integer range
       x = 32767 * (x - minX) * invSize;
       y = 32767 * (y - minY) * invSize;

       x = (x | (x << 8)) & 0x00FF00FF;
       x = (x | (x << 4)) & 0x0F0F0F0F;
       x = (x | (x << 2)) & 0x33333333;
       x = (x | (x << 1)) & 0x55555555;

       y = (y | (y << 8)) & 0x00FF00FF;
       y = (y | (y << 4)) & 0x0F0F0F0F;
       y = (y | (y << 2)) & 0x33333333;
       y = (y | (y << 1)) & 0x55555555;

       return x | (y << 1);
   }