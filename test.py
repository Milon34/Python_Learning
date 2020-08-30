num = input().split()
n,m,a = int(num[0]),int(num[1]),int(num[2])
if n%a != 0 :
    tile_wide = n//a + 1
else:
    tile_wide = n//a
# print(tile_wide)
if m%a != 0 :
    tile_long = m//a + 1
else:
    tile_long = m//a
# print(tile_long)
sum_tile = tile_wide * tile_long
print(sum_tile)