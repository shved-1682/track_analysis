import plotly.graph_objects as go

from data import list_721, list_722, list_724, list_725, list_727, list_728, list_730, list_731
import enum_classes
import update_graphics


def create_some_graphs(
        data_list: list,
        other_data_list: list
) -> None:
    for data, fl_rec_name_fd in zip(data_list, other_data_list):
        y_new, y_errors = update_graphics.count_metrics(data=data, ret2=True)

        x = list({fl_rec_name_fd[3], 10, 20, 30, 50, 75, 100})
        x.append(0) if len(x) == 6 else x.append(10)
        x = sorted(list(set(x)))

        y_errors = [error for error in y_errors if error != 0]
        start_y_error = len(x) - len(y_errors)

        fig = go.Figure()
        update_graphics.add_trace_go(
            flag=enum_classes.GraphFlag.error,
            fig=fig,
            list_y=y_new[start_y_error:],
            list_x=x[start_y_error:],
            list_y_error=y_errors[start_y_error:],
            name_fd_rec=fl_rec_name_fd[2],
            dash=fl_rec_name_fd[4],
            color=fl_rec_name_fd[5],
        )
        update_graphics.update_layout_go(
            fig=fig,
            title_text=f"PLOT: {fl_rec_name_fd[1]}pu composition {fl_rec_name_fd[2]}",
            xaxis_title="Percentage of deformation",
            yaxis_title="Density (1/мкм)",
        )
        fig.show()


def create_two_graph_3_5(
        data_list,
        other_data_list
) -> None:
    fig_pol_form3 = go.Figure()
    fig_pol_form5 = go.Figure()
    for data, fl_rec_name_fd in zip(data_list, other_data_list):
        y_new, y_errors = update_graphics.count_metrics(data=data, ret2=True)

        x = list({fl_rec_name_fd[3], 10, 20, 30, 50, 75, 100})
        x.append(0) if len(x) == 6 else x.append(10)
        x = sorted(list(set(x)))

        y_errors = [error for error in y_errors if error != 0]
        start_y_error = len(x) - len(y_errors)

        if fl_rec_name_fd[1] == enum_classes.PolForm.pol_formulation_3:
            update_graphics.add_trace_go(
                flag=enum_classes.GraphFlag.error,
                fig=fig_pol_form3,
                list_y=y_new[start_y_error:],
                list_x=x[start_y_error:],
                list_y_error=y_errors[start_y_error:],
                name_fd_rec=fl_rec_name_fd[2],
                color=fl_rec_name_fd[5],
            )
            update_graphics.update_layout_go(
                fig=fig_pol_form3,
                title_text=f"PLOT: 3pu composition",
                xaxis_title="Percentage of deformation (%)",
                yaxis_title="Density (1/мкм)",
                legend_title="Fluences (ион/см^2)",
            )
        elif fl_rec_name_fd[1] == enum_classes.PolForm.pol_formulation_5:
            update_graphics.add_trace_go(
                flag=enum_classes.GraphFlag.error,
                fig=fig_pol_form5,
                list_y=y_new[start_y_error:],
                list_x=x[start_y_error:],
                list_y_error=y_errors[start_y_error:],
                name_fd_rec=fl_rec_name_fd[2],
                color=fl_rec_name_fd[5],
            )
            update_graphics.update_layout_go(
                fig=fig_pol_form5,
                title_text="PLOT: 5pu composition",
                xaxis_title="Percentage of deformation (%)",
                yaxis_title="Density (1/мкм)",
                legend_title="Fluences (ион/см^2)",
            )
        else:
            pass
    fig_pol_form3.show()
    fig_pol_form5.show()


def create_one_graph(
        data_list,
        other_data_list
) -> None:
    fig = go.Figure()
    for data, fl_rec_name_fd in zip(data_list, other_data_list):
        y_new, y_errors = update_graphics.count_metrics(data=data, ret2=True)

        x = list({fl_rec_name_fd[3], 10, 20, 30, 50, 75, 100})
        x.append(0) if len(x) == 6 else x.append(10)
        x = sorted(list(set(x)))

        update_graphics.add_trace_go(
            flag=enum_classes.GraphFlag.error,
            fig=fig,
            list_y=y_new,
            list_x=x[len(x) - len(y_errors):],
            list_y_error=y_errors,
            name_fd_rec=f"{fl_rec_name_fd[2]}<br>{fl_rec_name_fd[1]}pu composition",
            dash=fl_rec_name_fd[4],
            color=fl_rec_name_fd[5],
        )
    update_graphics.update_layout_go(
        fig=fig,
        title_text=f"PLOT: All fluences",
        xaxis_title="Percentage of deformation (%)",
        yaxis_title="Density (1/мкм)",
        legend_title="Fluences (ион/см^2)"
    )
    fig.show()


def create_graph_fl_df(
        other_data_list=None
) -> None:
    x_5_3 = [name[2] for name in other_data_list][::-2]
    x = [
        "0,5*10^15", "1*10^15",
        "1,5*10^15", "2*10^15",
        "2,5*10^15", "3*10^15",
        "3,5*10^15", "4*10^15",
        "4,5*10^15", "5*10^15"
    ]
    y_5 = [50, 10, 3, 0]
    y_3 = [60, 13, 3, 0]
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    fig = go.Figure()
    for pol_form in [0, 5, 3]:
        if pol_form == enum_classes.PolForm.pol_formulation_5:
            update_graphics.add_trace_go(
                flag=enum_classes.GraphFlag.error,
                fig=fig,
                list_y=y_5,
                list_x=x_5_3,
                list_y_error=[error * 0.05 for error in y_5],
                name_fd_rec=f"{pol_form}pu composition",
                color="firebrick"
            )
        elif pol_form == enum_classes.PolForm.pol_formulation_3:
            update_graphics.add_trace_go(
                flag=enum_classes.GraphFlag.error,
                fig=fig,
                list_y=y_3,
                list_x=x_5_3,
                list_y_error=[error * 0.05 for error in y_3],
                name_fd_rec=f"{pol_form}pu composition",
                color="royalblue"
            )
        else:
            update_graphics.add_trace_go(
                flag=enum_classes.GraphFlag.line,
                fig=fig,
                list_y=y,
                list_x=x,
                mode='lines',
                name_fd_rec=f"X axis",
                color="rgb(255, 255, 255)"
            )
    update_graphics.update_layout_go(
        fig=fig,
        title_text=f"Breaking deformation 5pu, 3pu composition",
        xaxis_title="Fluence (ион/см^2)",
        yaxis_title="Breaking deformation (%)"
    )
    fig.show()


def create_derivative_graph(
        data_list,
        other_data_list
) -> None:
    fig = go.Figure()
    for data, fl_rec_name_fd in zip(data_list, other_data_list):
        y_new = update_graphics.count_metrics(data=data, ret2=False)
        y_new = update_graphics.derivative(y=y_new, name=fl_rec_name_fd[0])

        x = list({fl_rec_name_fd[3], 10, 20, 30, 50, 75, 100})
        x.append(0) if len(x) == 6 else x.append(10)
        x = sorted(list(set(x)))

        update_graphics.add_trace_go(
            flag=enum_classes.GraphFlag.line,
            fig=fig,
            list_y=y_new,
            list_x=x[len(x) - len(y_new):],
            name_fd_rec=f"{fl_rec_name_fd[2]}<br>{fl_rec_name_fd[1]}pu composition",
            dash=fl_rec_name_fd[4],
            color=fl_rec_name_fd[5],
        )
    update_graphics.update_layout_go(
        fig=fig,
        title_text=f"PLOT: derivative",
        xaxis_title="Percentage of deformation (%)",
        yaxis_title="Derivative",
        legend_title="Fluences (ион/см^2)"
    )
    fig.show()


def create_module_upr():
    pu = ['PU5', 'PU3']

    fig = go.Figure(
        data=[
            go.Bar(name="PU5",
                   x=[pu[0]],
                   y=[10]),
            go.Bar(name="PU3",
                   x=[pu[1]],
                   y=[30])
        ]
    )
    fig.update_layout(
        yaxis_title="Модуль упругости, МПа",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="black"
        )
    )
    fig.show()


main_data = [
    list_721,
    list_722,
    list_724,
    list_725,
    list_727,
    list_728,
    list_730,
    list_731
]
other_data = [
    (721, 5, "5*10^15", 0, "dash", "firebrick"),  # ион/см^2
    (722, 3, "5*10^15", 3, "solid", "firebrick"),
    (724, 5, "3*10^15", 0, "dash", "royalblue"),
    (725, 3, "3*10^15", 3, "solid", "royalblue"),
    (727, 5, "1*10^15", 10, "dash", "rgb(88, 235, 59)"),
    (728, 3, "1*10^15", 13, "solid", "rgb(88, 235, 59)"),
    (730, 5, "0,5*10^15", 50, "dash", "rgb(212, 132, 57)"),
    (731, 3, "0,5*10^15", 60, "solid", "rgb(212, 132, 57)")
]

# create_some_graphs(
#     data_list=main_data,
#     other_data_list=other_data
# )
# create_two_graph_3_5(
#     data_list=main_data,
#     other_data_list=other_data
# )
create_one_graph(
    data_list=main_data,
    other_data_list=other_data
)
create_graph_fl_df(
    other_data_list=other_data
)
create_derivative_graph(
    data_list=main_data,
    other_data_list=other_data
)
create_module_upr()
