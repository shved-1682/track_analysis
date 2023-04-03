import plotly.graph_objects as go
import numpy as np
import statistics

import enum_classes


def count_metrics(
        data,
        ret2):
    norm = [1, 1.1, 1.2, 1.3, 1.5, 1.75, 2]
    list_y = [list(my_d.values()) for my_d in data]
    list_y = [list(elem[0] + elem[1] + elem[2]) for elem in list_y]
    minq_maxq = [list(np.percentile(data, [25, 75])) for data in list_y]
    list_y_new = [
        sum(elem)/9/400*n
        for elem, n, qq in zip(
            list_y,
            norm,
            minq_maxq
        ) if sum(elem) != 0
    ]
    if ret2:
        list_y_error = [statistics.pstdev(elem)/400*n for elem, n in zip(list_y, norm)]
        list_y_error = [elem for elem in list_y_error if elem != 0]
        return list_y_new, list_y_error
    else:
        return list_y_new



# def count_metrics(data: list) -> (list, list):
#     density = []
#     norm = [1, 1.1, 1.2, 1.3, 1.5, 1.75, 2]
#     n = len(data)
#
#     y = np.array([list(my_d.values()) for my_d in data])
#     y = y.reshape(n, -1)
#     quantiles = np.percentile(y, [25, 75], axis=1)
#     errors = list(np.std(y, axis=1)*norm/400)
#     for i in range(n):
#         min_quantile, max_quantile = quantiles[:, i]
#         mask = (min_quantile <= y[i]) & (y[i] <= max_quantile)
#         density.append(y[i][mask].sum()/400/9*norm[i])
#
#     return density, errors


def derivative(
        y: list,
        name: int
):
    norm = [1, 1.1, 1.2, 1.3, 1.5, 1.75, 2]
    new_norm = []
    names = [721, 722, 724, 727, 730]
    derivative_y = []

    for i in range(len(norm)):
        if norm[i] != norm[-1]:
            new_norm.append(norm[i] - norm[i + 1])

    y = [el for el in y if el != 0]
    start_norm = len(norm) - len(y)
    new_norm = new_norm[start_norm:]

    for i, n in zip(range(len(y)), new_norm):
        if (y[i] != y[-1]) & (name in names):
            derivative_y.append(round((y[i] - y[i + 1])/n, 3))

    return derivative_y


def add_trace_go(
        flag=None,
        fig=None,
        list_y=None,
        list_x=None,
        list_y_error=None,
        name_fd_rec=None,
        mode="lines+markers",
        dash="solid",
        color="royalblue",
) -> None:
    if flag == enum_classes.GraphFlag.error:
        fig.add_trace(
            go.Scatter(
                x=list_x,
                y=list_y,
                error_y=dict(
                    type='data',
                    array=list_y_error,
                ),
                name=name_fd_rec,
                line=dict(
                    color=f'{color}',
                    dash=f'{dash}'
                )
            )
        )
    elif flag == enum_classes.GraphFlag.line:
        fig.add_trace(
            go.Scatter(
                x=list_x,
                y=list_y,
                name=name_fd_rec,
                mode=mode,
                line=dict(
                    color=f'{color}',
                    dash=f'{dash}'
                )
            )
        )
    else:
        pass


def update_layout_go(
        fig=None,
        title_text="",
        xaxis_title="",
        yaxis_title="",
        legend_title="",
) -> None:
    fig.update_layout(
        title={
            'text': title_text,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
        legend_title=legend_title,
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="black"
        )
    )
