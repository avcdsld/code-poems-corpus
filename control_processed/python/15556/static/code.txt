def plot_compare_curves(image_list, method_list, color_list, compare_dict, fig_name="", fig_num=111):
    """绘制对比曲线."""
    plt.subplot(fig_num)
    plt.title(fig_name, loc="center")  # 设置绘图的标题
    mix_ins = []
    for index, method in enumerate(method_list):
        mem_ins = plt.plot(image_list, compare_dict[method], "-", label=method, color=color_list[index], linestyle='-', marker='.')
        # mem_ins = plt.plot(image_list, compare_dict[method], "-", label=method, color='deepskyblue', linestyle='-', marker='.')
        mix_ins.append(mem_ins)

    plt.legend(loc='upper right')  # 说明标签的位置
    plt.grid()  # 加网格
    # plt.xlabel("Image")
    plt.ylabel("Mem(MB)")
    plt.ylim(bottom=0)