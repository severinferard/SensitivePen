import matplotlib.pyplot as plt

def plotdata(df, integral, derivate, angle):

    fig = plt.figure(figsize=(25,10))
    ax1 = fig.add_subplot(1, 3, 1)
    ax2 = fig.add_subplot(1, 3, 2)
    ax3 = fig.add_subplot(1,3,3)
    fig.tight_layout(pad=3)
    ax1.plot(df['time'], integral, label='Integral Acc')
    ax2.plot(df['time'], derivate, label='Derivate Acc')
    ax3.plot(df['time'], angle, label='Angle XZ')
    ax1.set_xlabel('Time (mS)')
    ax1.set_ylabel('Int')
    ax1.set_title('Integral')
    ax1.legend()
    ax2.set_xlabel('Time (mS)')
    ax2.set_ylabel('Int')
    ax2.set_title('Derivate')
    ax2.legend()
    ax3.set_xlabel('Time (mS)')
    ax3.set_ylabel('Value')
    ax3.set_title('Angle')
    plt.show()

def plotfeatures(dfinal):
    fig = plt.figure(figsize=(25, 10))
    ax1 = fig.add_subplot(2, 3, 1)
    ax2 = fig.add_subplot(2, 3, 2)
    ax3 = fig.add_subplot(2, 3, 3)
    ax4 = fig.add_subplot(2,3,4)
    ax5 = fig.add_subplot(2,3,5)
    ax6 = fig.add_subplot(2,3,6)
    fig.tight_layout(pad=3)
    rect = fig.patch
    rect.set_facecolor('#B4BAD6')
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.spines['top'].set_visible(False)
    ax4.spines['right'].set_visible(False)
    ax4.spines['top'].set_visible(False)
    ax5.spines['right'].set_visible(False)
    ax5.spines['top'].set_visible(False)
    ax6.spines['right'].set_visible(False)
    ax6.spines['top'].set_visible(False)
    ax1.scatter(dfinal['DC'], dfinal['Deviation'],  c=dfinal.target, marker='o', alpha= 0.5)
    ax2.scatter(dfinal['DC'], dfinal['energy'],c=dfinal.target,marker='o', alpha= 0.5)
    ax3.scatter(dfinal['DC'], dfinal['entropyDFT'],c=dfinal.target, marker='o', alpha= 0.5)
    ax4.scatter(dfinal['energy'], dfinal['entropyDFT'],c=dfinal.target, marker='o', alpha= 0.5)
    ax5.scatter(dfinal['energy'], dfinal['Deviation'],c=dfinal.target, marker='o', alpha= 0.5)
    ax6.scatter(dfinal['entropyDFT'], dfinal['Deviation'],c=dfinal.target, marker='o', alpha= 0.5)
    ax1.set_xlabel('DC')
    ax1.set_ylabel('Deviation')
    ax1.set_title('DC x Deviation')
    ax1.legend()
    ax2.set_xlabel('DC')
    ax2.set_ylabel('Energy')
    ax2.set_title('DC x Energy')
    ax2.legend()
    ax3.set_xlabel('DC')
    ax3.set_ylabel('entropyDFT')
    ax3.set_title('DC x entropyDFT')
    ax3.legend()
    ax4.set_xlabel('Energy')
    ax4.set_ylabel('entropyDFT')
    ax4.set_title('Energy x EntropyDFT')
    ax4.legend()
    ax5.set_xlabel('Energy')
    ax5.set_ylabel('Deviation')
    ax5.set_title('Energy x Deviation')
    ax5.legend()
    ax6.set_xlabel('entropyDFT')
    ax6.set_ylabel('Deviation')
    ax6.set_title('entropyDFT x Deviation')
    ax6.legend()
    plt.show()

def plotfeaturesnotarget(dfinal):
    fig = plt.figure(figsize=(25, 10))
    ax1 = fig.add_subplot(2, 3, 1)
    ax2 = fig.add_subplot(2, 3, 2)
    ax3 = fig.add_subplot(2, 3, 3)
    ax4 = fig.add_subplot(2, 3, 4)
    ax5 = fig.add_subplot(2, 3, 5)
    ax6 = fig.add_subplot(2, 3, 6)
    fig.tight_layout(pad=3)
    rect = fig.patch
    rect.set_facecolor('#B4BAD6')
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.spines['top'].set_visible(False)
    ax4.spines['right'].set_visible(False)
    ax4.spines['top'].set_visible(False)
    ax5.spines['right'].set_visible(False)
    ax5.spines['top'].set_visible(False)
    ax6.spines['right'].set_visible(False)
    ax6.spines['top'].set_visible(False)
    ax1.scatter(dfinal['DC'], dfinal['Deviation'], marker='o', alpha=0.5)
    ax2.scatter(dfinal['DC'], dfinal['energy'], marker='o', alpha=0.5)
    ax3.scatter(dfinal['DC'], dfinal['entropyDFT'], marker='o', alpha=0.5)
    ax4.scatter(dfinal['energy'], dfinal['entropyDFT'], marker='o', alpha=0.5)
    ax5.scatter(dfinal['energy'], dfinal['Deviation'], marker='o', alpha=0.5)
    ax6.scatter(dfinal['entropyDFT'], dfinal['Deviation'], marker='o', alpha=0.5)
    ax1.set_xlabel('DC')
    ax1.set_ylabel('Deviation')
    ax1.set_title('DC x Deviation')
    ax1.legend()
    ax2.set_xlabel('DC')
    ax2.set_ylabel('Energy')
    ax2.set_title('DC x Energy')
    ax2.legend()
    ax3.set_xlabel('DC')
    ax3.set_ylabel('entropyDFT')
    ax3.set_title('DC x entropyDFT')
    ax3.legend()
    ax4.set_xlabel('Energy')
    ax4.set_ylabel('entropyDFT')
    ax4.set_title('Energy x EntropyDFT')
    ax4.legend()
    ax5.set_xlabel('Energy')
    ax5.set_ylabel('Deviation')
    ax5.set_title('Energy x Deviation')
    ax5.legend()
    ax6.set_xlabel('entropyDFT')
    ax6.set_ylabel('Deviation')
    ax6.set_title('entropyDFT x Deviation')
    ax6.legend()
    plt.show()


