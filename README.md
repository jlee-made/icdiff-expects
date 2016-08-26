# icdiff-expects

icdiff-expects is an expects matcher that uses
[this fork of icdiff](https://github.com/jlee-made/icdiff) -- to make equality
test assertion failures in Python tests that use the
[expects assertion library](https://pypi.python.org/pypi/expects) print
readable intraline coloured diffs.


## Install

To install from the latest release on PyPI:

```
pip install icdiff-expects
```

## Use

In your test code (e.g. a unittest test case method):

    from expects import expect
    import icdiff_expects

    ...

    expect = {
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
    expect(got).to(icdiff_expects.equal(got))
