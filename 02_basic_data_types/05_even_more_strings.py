lyric = 'Sometimes is seen a strange spot in the sky...'
lyric = lyric.lower()

s_count = lyric.count('s')
print(s_count)

print('Our lyric has', s_count, "s' in it.")

print('Our lyric has ' + str(s_count) + " s' in it.")
# print(f"Our lyric has {str(s_count)} s' in it.")
print("Our lyric has", s_count, "s' in it.", sep=":)")