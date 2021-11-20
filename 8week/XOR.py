print(
    *list(
        map(
            lambda arr: abs(arr[0] - arr[1]),
            zip(
                map(int, input().split()),
                map(int, input().split())
            )
        )
    )
)
