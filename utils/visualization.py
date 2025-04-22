import matplotlib.pyplot as plt


def init_plot(scl_a4: int = 1, aspect_ratio: list[str] = [3,2], page_lnewdth_cm: int = 15, fnt: str = 'serif', mrksze: int = 2, lnewdth: int = 1, fontsize: int = 10, labelfontsize: int = 9, tickfontsize: int = 8, dpi: int = 300) -> None:
    """
    Overrides the default configuration for plotting.

    Args:
        scl_a4 (int, optional): Scale of the image relative to a full page. Defaults to 1.
            - 1 for full-page figure.
            - 2 for half-page figure.
        aspect_ratio (list, optional): Aspect ratio (width to height) of the figure. Defaults to [3,2].
        page_lnewdth_cm (int, optional): Width of the page (in cm) excluding margins. Defaults to 15.
        fnt (str, optional): Font family to be used in the figure. Defaults to 'serif'.
        mrksze (int, optional): Marker size to be used in the figure. Defaults to 2.
        lnewdth (int, optional):Line width to be used in the figure. Defaults to 1.
        fontsize (int, optional): Base font size to be used in the figure. Defaults to 10.
        labelfontsize (int, optional): Font size for axis labels. Defaults to 9.
        tickfontsize (int, optional): Font size for the tick labels. Defaults to 8.
        dpi (int, optional): Resolution of the figure when exported to image formats. Defaults to 300.
    """
    # --- Calculate figure size in inches ---
    # scl_a4=2: Half page figure
    if scl_a4 == 2:     
        fac = page_lnewdth_cm/(2.54*aspect_ratio[0]*2) #2.54: cm --> inch
        figsze = [aspect_ratio[0]*fac, aspect_ratio[1]*fac]

    # scl_a4=1: Full page figure
    elif scl_a4 == 1:
        fac = page_lnewdth_cm/(2.54*aspect_ratio[0]) #2.54: cm --> inch
        figsze = [aspect_ratio[0]*fac, aspect_ratio[1]*fac]

    # --- Initialize defaults ---
    plt.rcdefaults()

    # --- General plot setup ---
    # font
    plt.rcParams['font.family'] = fnt

    # figure
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['figure.figsize'] = figsze
    plt.rcParams['figure.dpi'] = dpi

    # axes
    plt.rcParams['axes.labelsize'] = labelfontsize
    plt.rcParams['axes.linewidth'] = 0.5
    plt.rcParams['axes.titlesize'] = fontsize
    plt.rcParams['axes.axisbelow'] = True
    plt.rcParams['axes.grid'] = True
    plt.rcParams['axes.grid.which'] = 'both'

    # lines
    plt.rcParams['lines.markersize'] = mrksze
    plt.rcParams['lines.linewidth'] = lnewdth

    # hatch
    plt.rcParams['hatch.linewidth'] = lnewdth/2

    # ticks
    plt.rcParams['xtick.labelsize'] = tickfontsize
    plt.rcParams['xtick.direction'] = 'inout'
    plt.rcParams['ytick.labelsize'] = tickfontsize
    plt.rcParams['ytick.direction'] = 'inout'

    # legend
    plt.rcParams['legend.fontsize'] = fontsize
    plt.rcParams['legend.fancybox'] = True
    plt.rcParams['legend.facecolor'] = 'white'
    plt.rcParams['legend.shadow'] = False
    plt.rcParams['legend.edgecolor'] = 'black'
    plt.rcParams['legend.handletextpad'] = 0.2
    plt.rcParams['legend.handlelength'] = 1
    plt.rcParams['legend.borderpad'] = 0.2
    plt.rcParams['legend.labelspacing'] = 0.2
    plt.rcParams['legend.columnspacing'] = 0.2

    #grid
    plt.rcParams['grid.linewidth'] = 0.5

    # mathtext
    plt.rcParams['mathtext.fontset'] = 'cm'