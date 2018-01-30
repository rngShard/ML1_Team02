import matplotlib.pyplot as plt

class PoliticalCompass:
    def __init__(self):
        #plot the seven deadly parties
        # self.__parties_x = [3,2,4,5.5,7,8,-5]
        # self.__parties_y = [2,4,7,8,3,5.5,-5]
        # self.__parties_names = ['SPD', 'Die Grunen' , 'CSU', 'AFD', 'FDP', 'CDU','Die Linke']
        # self.__parties_colors = ['r','g','c','b','y','k','m']

        self.__parties_x = [4,7,5,2,-5,3,8]
        self.__parties_y = [7,5,3,4,-5,2,5.5]
        self.__parties_names = ['CSU', 'FDP', 'AFD', 'Die Grunen', 'Die Linke', 'SPD', 'CDU' ]
        self.__parties_colors = ['c','y', 'b', 'g', 'm', 'r','k']

    def plotPoliticianInCompass(self, party_name,politician_name_list, probabilities_list):
        #draw the given poltician position
        #TODO: the new_user point color should be a mixture of the colors of the parties 
        #according to his given probabilities
        for i in range(0, len(politician_name_list)):
            fig, ax = plt.subplots()
            #draw the seven major parties
            ax.scatter(self.__parties_x, self.__parties_y, c =self.__parties_colors)
            for i, self.__parties_names in enumerate(self.__parties_names):
                ax.annotate(self.__parties_names, (self.__parties_x[i],self.__parties_y[i]))

                
                politician_x = 0
                politician_y = 0
                for j in range(0,len(probabilities_list[i])):
                    politician_x += probabilities_list[i][j] * self.__parties_x[j]
                    politician_y += probabilities_list[i][j] * self.__parties_y[j]
                ax.scatter(politician_x,politician_y)
                ax.annotate(politician_name_list[i],(politician_x,politician_y))

            #centerize the compass axes
            ax.spines['left'].set_position('center')
            ax.spines['right'].set_color('none')
            ax.spines['bottom'].set_position('center')
            ax.spines['top'].set_color('none')
            ax.spines['left'].set_smart_bounds(True)
            ax.spines['bottom'].set_smart_bounds(True)
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')

            #add compass labels
            plt.text(8,1,"Right")
            plt.text(-6,1,"Left")
            plt.text(1,8.5,"Authoritarian")
            plt.text(1,-6,"Libertarian")

            #hide tick labels
            ax.set_yticklabels([])
            ax.set_xticklabels([])

            plt.gcf().canvas.set_window_title('Political Compass')
            plt.savefig(party_name+'/'+politician_name_list[i]+'.png')

