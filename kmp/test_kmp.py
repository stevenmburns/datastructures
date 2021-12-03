# Python program for KMP Algorithm

def computeLPSArray(pat):
    M = len(pat)
    lps = [0]*M

    assert 0 == lps[0] # lps[0] is always 0
    i, l = 1, 0 # length of the previous longest prefix suffix
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if l != 0:
                l = lps[l-1]
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1

    assert 0 == lps[0] # lps[0] is always 0
    return lps

def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
  
    # Preprocess the pattern (calculate lps[] array)
    lps = computeLPSArray(pat)

    print(pat, list(zip(pat,lps)))
  
    i, j = 0, 0 # index for txt[], index for pat[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if j == M:
            yield i-j
            j = lps[j-1]
  
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1



# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book
  
# d is the number of characters in the input alphabet

  
# pat  -> pattern
# txt  -> text
# q    -> A prime number
  
def RKSearch(pat, txt):
    d = 256
    q = 101
    M = len(pat)
    N = len(txt)

    if M > N:
        return
  
    h = pow(d, M, q)

    p, t = 0, 0
    for a,b in zip(pat,txt):
        p = (d * p + ord(a))% q
        t = (d * t + ord(b))% q
  
    # Slide the pattern over text one by one
    for i in range(N-M + 1):
        if p == t: # hash match
            if txt[i:i+M] == pat:
                yield i
        if i < N-M: # compute new hash value
            t = (d*t-ord(txt[i])*h + ord(txt[i + M]))% q

  
Search = RKSearch
  

def test_A0():
  
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    assert list(Search(pat, txt)) == [10]
  
def test_A1():
  
    txt = "aaaaaaaaaaaaaaaaaa"
    pat = "steve burns is a treefrog yes steve burns is a treefrog"
    assert list(Search(pat, txt)) == []