# icdiff-expects

icdiff-expects is an expects matcher that uses
[this fork of icdiff](https://github.com/jlee-made/icdiff) -- to make equality
test assertion failures in Python tests that use the
[expects assertion library](https://pypi.python.org/pypi/expects) print
readable intraline coloured diffs.


## Install

I haven't got around to releasing this on PyPI, but you can put this in a
requirements.txt:

```
-e git+https://github.com/jlee-made/icdiff-expects.git@04c834cc6968aab367e2f1f2c0d72faf6d920985#egg=icdiff-expects
-e git+https://github.com/jlee-made/icdiff.git@13abb1ae6120f31edcf856c7468268f1eeff6cea#egg=icdiff-inprocess
```

and then `pip install -r requirements.txt`

## Use

In your test code (e.g. a unittest test case method):

    from expects import expect
    import icdiff_expects

    ...

    expected = {
        "spam_id": "32102903",
        "spam_code": "spam",
        "spam_count": 4295,
        "spam_method": "thorough",
        "spam_type": "full",
        "spamspamspamspam": "2016-08-26T15:20:12Z",
        "spam_transaction": "ABS32402983SAJFDAJFS"
    }
    got = {
        "spam_id": "32102903",
        "spam_code": "spam",
        "spam_method": "thorough",
        "spam_type": "full",
        "spamspamspamspam": "2016-08-26T15:21:12Z",
        "spam_transaction": "ABS32402983SAJFDAJFS"
    }
    expect(expected).to(icdiff_expects.equal(got))
