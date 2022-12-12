import sys
from tokenize import Token
from .documents import Documents


def error(
    documents: Documents,
    context: str,
    token: Token,
    message: str,
    error: str = "Error",
) -> None:
    data = documents.by_id[token.document].content
    cnt = 1
    idx = 0
    start = 0
    t = 0
    while idx < token.index:
        if data[idx] == "\n":
            cnt += 1
            start = idx + 1
            t = 0
        if data[idx] == "\t":
            t += 1
        idx += 1
    print(
        "%s:%s: %s in %s: %s"
        % (documents.by_id[token.document].path, cnt, error, context, message),
        file=sys.stderr,
    )
    end = start
    while end < len(data) and data[end] != "\n":
        end += 1
    print(data[start:end], file=sys.stderr)
    print(
        "%s%s%s" % ("\t" * t, " " * (token.index - start - t), "^" * (token.length)),
        file=sys.stderr,
    )
