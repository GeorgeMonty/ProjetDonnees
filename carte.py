
import numpy as np
import shapefile as shp
import matplotlib.pyplot as plt
import matplotlib.colors as clrs
import matplotlib.cm as cm
import os
from jellyfish import levenshtein_distance
from statistique import Statistique


class CartoPlot:
    '''Class providing an easy way to plot geographic data.

    Based on département and région shapes of France.

    Parameters
    ----------
    departement_shp_path : str
        path to the shapefile (.shp) with the départements
    regions_shp_path : str
        path to the shapefile (.shp) with régions

    Attributes
    ----------
    __sf_dep : shapefile.Reader
        shapefile data for départements
    __sf_reg : shapefile.Reader
        shapefile data for régions
    __cmap : matplotlib.colors.Colormap
        colormap to use to fill the shapes with

    Examples
    --------
    >>> cp = CartoPlot()

    >>> d = {}
    >>> d['Betagni'] = 1
    >>> fig = cp.plot_reg_map(data=d)
    >>> fig.show()
    >>> fig.savefig('regions.test.jpg')

    >>> d = {}
    >>> for i in range(1, 96):
    >>>     d[str(i)] = i
    >>> del(d['69'])
    >>> d['69D'] = 69
    >>> d['69M'] = 69
    >>> d['2A'] = 20
    >>> d['2B'] = 20.5
    >>> fig = cp.plot_dep_map(data=d, x_lim=(-6, 10), y_lim=(41, 52))
    >>> fig.show()
    >>> fig.savefig('departements.test.jpg')
    '''

    def __init__(self,departement_shp_path=os.path.join(os.path.dirname(os.path.abspath("C:/Users/camil/Documents/ensai/1A/projet_traitementdonnees/classe2")), 'departements-20180101.shp'),regions_shp_path=os.path.join(os.path.dirname(os.path.abspath("C:/Users/camil/Documents/ensai/1A/projet_traitementdonnees/classe2")), 'regions-20180101.shp'), colormap='viridis'):
        '''Create the object and gather the data on département and régions.

        Parameters
        ----------
        departement_shp_path : str
            path to the shapefile (.shp) with the départements
        regions_shp_path : str
            path to the shapefile (.shp) with régions
        colormap : str or matplotlib.colors.Colormap = 'viridis'
            argument to get a colormap using matplotlib.cm.get_cmap()
        
        Examples
        --------
        >>> cp = CartoPlot()
        '''
        self.__sf_dep = shp.Reader("C:/Users/camil/Documents/ensai/1A/projet_traitementdonnees/classe2/departements-20180101.shp")
        self.__sf_reg = shp.Reader("C:/Users/camil/Documents/ensai/1A/projet_traitementdonnees/classe2/regions-20180101.shp")
        self.__cmap = plt.get_cmap(colormap)
        
        
    def dictionnaire_dep(self,classification):
        '''Transforme le array numpy de la classification en dictionnaire pour les départements


        Parameters
        ----------
        classification : array numpy
            l'array numpy à convertir en dictionnaire. 

        Returns
        -------
        d : dictionnaire
            le dictionnaire avec en clé le numéro du département et en valeur le numéro de la classe.
        
        Examples
        --------
        >>> cp = CartoPlot()
        >>> classification = np.array([0., 2., 2., 2., 2., 1., 0., 2., 2., 2., 2., 2., 1., 2., 2., 2., 2., 2., 2., 0., 2., 2., 2., 2., 0., 2., 2., 0., 2., 2., 0., 0., 2., 0., 1., 0., 2., 0., 0., 2., 2., 2., 0., 2., 0., 0., 2., 2., 2., 0., 2., 2., 2., 2., 0., 2., 0., 0., 2., 1., 0., 2., 0., 0., 1., 2., 2., 1., 1., 1., 2., 0., 0., 2., 0., 1., 1., 0., 1., 2., 0., 2., 2., 1., 0., 2., 2., 2., 2., 2., 2., 1., 1., 1., 1., 0., 2., 2., 2., 2.,2.])
        >>> cp.dictionnaire_dep(classification)
        >>>{'1': 0.0, '2': 2.0, '3': 2.0, '4': 2.0, '5': 2.0, '6': 1.0, '7': 0.0, '8': 2.0, '9': 2.0, '10': 2.0, '11': 2.0, '12': 2.0, '13': 1.0, '14': 2.0, '15': 2.0, '16': 2.0, '17': 2.0, '18': 2.0, '19': 2.0, '21': 0.0, '22': 2.0, '23': 2.0, '24': 2.0, '25': 2.0, '26': 0.0, '27': 2.0, '28': 2.0, '29': 0.0, '30': 0.0, '31': 0.0, '32': 2.0, '33': 0.0, '34': 1.0, '35': 0.0, '36': 2.0, '37': 0.0, '38': 0.0, '39': 2.0, '40': 2.0, '41': 2.0, '42': 0.0, '43': 2.0, '44': 0.0, '45': 0.0, '46': 2.0, '47': 2.0, '48': 2.0, '49': 0.0, '50': 2.0, '51': 2.0, '52': 2.0, '53': 2.0, '54': 0.0, '55': 2.0, '56': 0.0, '57': 0.0, '58': 2.0, '59': 1.0, '60': 0.0, '61': 2.0, '62': 0.0, '63': 0.0, '64': 1.0, '65': 2.0, '66': 2.0, '67': 1.0, '68': 1.0, '70': 2.0, '71': 0.0, '72': 0.0, '73': 2.0, '74': 0.0, '75': 1.0, '76': 1.0, '77': 0.0, '78': 1.0, '79': 2.0, '80': 0.0, '81': 2.0, '82': 2.0, '83': 1.0, '84': 0.0, '85': 2.0, '86': 2.0, '87': 2.0, '88': 2.0, '89': 2.0, '90': 2.0, '91': 1.0, '92': 1.0, '93': 1.0, '94': 1.0, '95': 0.0, '2A': 2.0, '2B': 2.0, '69D': 1.0, '69M': 1.0, '971': 2.0, '972': 2.0, '973': 2.0, '974': 2.0, '976': 2.0}
        '''
    
        d={}
        for i in range(1,20):
            d[str(i)]= classification[i-1]
        for i in range(21,30):
            d[str(i)]=classification[i-2]
        for i in range(30,96):
            d[str(i)]= classification[i]
        d['2A']=classification[28]
        d['2B']=classification[29]
        del(d['69'])
        d['69D'] = classification[69]
        d['69M'] = classification[69]
        d['971']=classification[96]
        d['972']=classification[97]
        d['973']=classification[98]
        d['974']=classification[99]
        d['976']=classification[100]
        return d


    def dictionnaire_reg(self,classification):
        """Transforme le array numpy de la classification en dictionnaire pour les régions
        

        Parameters
        ----------
        classification : array numpy
            l'array numpy contenant le numéro de la classe à laquelle appartiennent chaque région

        Returns
        -------
        d : dictionnaire
            une dictionnaire qui associe le nom de la région au numéro de la classe à laquelle elle appartient.
        
        Examples
        --------
        >>> cp = CartoPlot()
        >>> classification = np.array([0., 2., 2., 2., 2., 1., 0., 2., 2., 2., 2., 2., 1., 2., 2., 2., 2., 2.])
        >>> cp.dictionnaire_reg(classification)
        >>> {'Auvergne-Rhône-Alpes': 0.0, 'Bourgogne-Franche-Comté': 2.0, 'Bretagne': 2.0, 'Centre-Val de Loire': 2.0, 'Corse': 2.0, 'Grand-Est': 1.0, 'Guadeloupe': 0.0, 'Guyane': 2.0, 'Hauts-de-France': 2.0, 'Ile-de-France': 2.0, 'La Réunion': 2.0, 'Martinique': 2.0, 'Mayotte': 1.0, 'Normandie': 2.0, 'Nouvelle-Aquitaine': 2.0, 'Occitanie': 2.0, 'Pays de la Loire': 2.0, "Provence-Alpes-Côte d'Azur": 2.0}

        """
        d={}
        d["Auvergne-Rhône-Alpes"]=classification[0]
        d["Bourgogne-Franche-Comté"]=classification[1]
        d["Bretagne"]=classification[2]
        d["Centre-Val de Loire"]=classification[3]
        d["Corse"]=classification[4]
        d["Grand-Est"]=classification[5]
        d["Guadeloupe"]=classification[6]
        d["Guyane"]=classification[7]
        d["Hauts-de-France"]=classification[8]
        d["Ile-de-France"]=classification[9]
        d["La Réunion"]=classification[10]
        d["Martinique"]=classification[11]
        d["Mayotte"]=classification[12]
        d["Normandie"]=classification[13]
        d["Nouvelle-Aquitaine"]=classification[14]
        d["Occitanie"]=classification[15]
        d["Pays de la Loire"]=classification[16]
        d["Provence-Alpes-Côte d'Azur"]=classification[17]
        return d

    def plot_reg_map(self, data={}, show_name=True, d_lim=(None, None), x_lim=None, y_lim=None, figsize=(11, 9)):
        '''Plot France's map with Régions and optional data.

        Possibility to set the axes limits to restrict to a subarea.

        Parameters
        ----------
        data : dictionnary = {}
            the dictionnary with the data to convert to a list. Keys correspond to régions
        show_name : bool = True
            whether to show the name of the internal identifier of the régions
        d_lim : tuple = (None, None)
            data limits for the colormap. If None, max and/or min are computed and used
        x_lim : tuple = None
            spatial limits (longitude min, longitude max)
        y_lim : tuple = None
            spatial limits (latitude min, latitude max)
        figsize : tuple = (11, 9)
            size of the figure

        Returns
        -------
        matplotlib.figure.Figure
            figure objet from matplotlib with the map of the régions and the data

        Examples
        --------
        >>> cp = CartoPlot()
        >>> d = {}
        >>> d['Betagni'] = 1
        >>> fig = cp.plot_reg_map(data=d)
        >>> fig.show()
        '''
        nrm = CartoPlot.__normalizer(data, d_lim)

        return CartoPlot.__plot_map_base(
                self.__sf_reg,
                data=CartoPlot.__data_list(
                    self.__sf_reg,
                    1,
                    data,
                    nrm=nrm),
                cmap=self.__cmap,
                nrm=nrm,
                x_lim=x_lim,
                y_lim=y_lim,
                figsize=figsize,
                label_record_idx=1 if show_name else 0)

    def plot_dep_map(self, data={}, show_name=False, d_lim=(None, None), x_lim=None, y_lim=None, figsize=(11, 9)):
        '''Plot France's map with Départments and optional data.

        Possibility to set the axes limits to restrict to a subarea.

        Parameters
        ----------
        data : dictionnary
            the dictionnary with the data to convert to a list. Keys correspond to départements
            identifiers (such as '35' for 'Ille et Vilaine', or '2B' for 'Haute Corse')
        show_name : bool = True
            whether to show the name of the internal identifier of the déparements
        d_lim : tuple = (None, None)
            data limits for the colormap. If None, max and/or min are computed and used
        x_lim : tuple = None
            spatial limits (longitude min, longitude max)
        y_lim : tuple = None
            spatial limits (latitude min, latitude max)
        figsize : tuple = (11, 9)
            size of the figure

        Returns
        -------
        matplotlib.figure.Figure
            figure objet from matplotlib with the map of the départements and the data

        Examples
        --------
        >>> cp = CartoPlot()
        >>> d = {}
        >>> d['35'] = 1
        >>> fig = cp.plot_dep_map(data=d)
        >>> fig.show()
        '''
        # Preprocess départements to pad them with zeros when needed
        data = dict(zip(['0{}'.format(x) if len(x) < 2 else x for x in data.keys()], data.values()))

        nrm = CartoPlot.__normalizer(data, d_lim)

        return CartoPlot.__plot_map_base(
                self.__sf_dep,
                data=CartoPlot.__data_list(
                    self.__sf_dep,
                    0,
                    data,
                    levenshtein_threshold=3 if show_name else 0,
                    nrm=nrm),
                cmap=self.__cmap,
                nrm=nrm,
                x_lim=x_lim,
                y_lim=y_lim,
                figsize=figsize,
                label_record_idx=1 if show_name else 0)

    @staticmethod
    def __normalizer(data, d_lim=(None, None)):
        '''Create an object to normalize data

        Parameters
        ----------
        data : dict
            the dictionnary with the data to convert to a list. Keys correspond to shapes
        d_lim : tuple = (None, None)
            data limits for the colormap. If None, max and/or min are computed and used

        Returns
        -------
        matplotlib.colors.Normalize
            the matplotlib object to normalize data
        '''
        # Initialize the data normalization object
        d_min, d_max = d_lim
        if d_lim[0] is None:
            d_min = min(data.values())
        if d_lim[1] is None:
            d_max = max(data.values())
        nrm = clrs.Normalize(vmin=d_min, vmax=d_max, clip=True)

        return nrm

    @staticmethod
    def __data_list(sf, record_idx, data, levenshtein_threshold=3, nrm=clrs.Normalize(0, 1, True)):
        '''Convert a data dictionnary to a data list

        This static method can be modified and adapted to the choice of data type for the
        variable data.

        Parameters
        ----------
        sf : shapefile.Reader
            the variable holding the shapefile data
        record_idx : int
            the index in the shape record pointing to the record name to match the data keys
        data : dict
            the dictionnary with the data to convert to a list. Keys correspond to shapes
        levenshtein_threshold : int = 3
            threshold to consider the string approximately equal in the Levenshtein distance
        nrm : matplotlib.colors.Normalize = matplotlib.colors.Normalize(0, 1, True)
            the matplotlib object to normalize data

        Returns
        -------
        list
            data list with indices corresponding to shapes in the shapefile, to be used in
            __plot_map_base()
        '''
        # Initialise the output to the right size
        data_list = [None] * len(sf.shapeRecords())

        # Loop through the shapes
        for shape_idx, shape in enumerate(sf.shapeRecords()):
            # Get the record name we want the keys of the dictionnary to match to
            rec_idx = shape.record[record_idx]

            # Two possibilities: exact or approximate match
            if rec_idx in data:
                data_list[shape_idx] = nrm(data[rec_idx])
            elif levenshtein_threshold > 0:
                # Using Levenshtein distance to allow for some discrepancy
                for data_key, data_value in data.items():
                    if levenshtein_distance(data_key, rec_idx) <= levenshtein_threshold:
                        data_list[shape_idx] = nrm(data_value)
                        break
                
        return data_list

    @staticmethod
    def __plot_map_base(sf, data=[], nrm=clrs.Normalize(0, 1, True), cmap=plt.get_cmap('viridis'), x_lim=None, y_lim=None, figsize=(11, 9), label_record_idx=0):
        '''Base function to plot shapes to form a map, and data to shade those shapes.

        The variable data could be changed to fit whatever type is needed in the project.

        Parameters
        ----------
        data : list = []
            data list with indices corresponding to shapes in the shapefile, to be used in
            __plot_map_base()
        nrm : matplotlib.colors.Normalize = matplotlib.colors.Normalize(0, 1, True)
            the matplotlib object to normalize data
        cmap : matplotlib.colors.Colormap = matplotlib.pyplot.get_cmap('viridis')
            colormap to use to fill the shapes with
        x_lim : tuple = None
            spatial limits (longitude min, longitude max)
        y_lim : tuple = None
            spatial limits (latitude min, latitude max)
        figsize : tuple = (11, 9)
            size of the figure
        label_record_idx : int = 0
            the index of the label to plot in the shapes' records

        Returns
        -------
        matplotlib.figure.Figure
            figure objet from matplotlib with the map of the départements and the data
        '''
        # Figure preparation
        fig = plt.figure(figsize=figsize)
        fig.clf()

        # Axes prepration, with no frame and no ticks
        ax = fig.add_subplot(1, 1, 1, frame_on=False)
        ax.tick_params(left=False,
                       bottom=False,
                       labelleft=False,
                       labelbottom=False)
        # For older versions of matplotlib requiring to set some array
        sm = cm.ScalarMappable(norm=nrm, cmap=cmap)
        sm.set_array([])
        fig.colorbar(sm, ax=ax)
        
        # Go through all shapes
        for shape_idx, shape in enumerate(sf.shapeRecords()):
            # Go through all parts (islands and such)
            start_part = 0
            for start_next_part in list(shape.shape.parts[1:]) + [len(shape.shape.points)]:
                x = [i[0] for i in shape.shape.points[start_part:start_next_part]]
                y = [i[1] for i in shape.shape.points[start_part:start_next_part]]
                ax.plot(x, y, 'k')
                if len(data) > 0 and data[shape_idx] is not None:
                    ax.fill(x, y, clrs.rgb2hex(cmap(data[shape_idx])))
                start_part = start_next_part

            # Find the center point of the shape
            x = [i[0] for i in shape.shape.points]
            y = [i[1] for i in shape.shape.points]
            x0 = np.mean([min(x), max(x)])
            y0 = np.mean([min(y), max(y)])

            # Add the shape's label
            ax.text(x0, y0, shape.record[label_record_idx], fontsize=10, horizontalalignment='center')

        # The the axes limits
        if (x_lim is not None) and (y_lim is not None):     
            ax.set_xlim(x_lim)
            ax.set_ylim(y_lim)

        return fig


