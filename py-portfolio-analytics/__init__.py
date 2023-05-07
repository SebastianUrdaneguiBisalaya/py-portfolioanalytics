# Librerías para importar las funciones que serán necesarias para la construcción del reporte
from functions.functions import get_stock_price_close
from functions.functions import get_name_columns
from functions.functions import get_date_start
from functions.functions import get_date_end
from functions.functions import plot_return_log
from functions.functions import histogram_stock_returns
from functions.functions import return_log_mean_and_standard_deviation
from functions.functions import plot_covariance_matrix
from functions.functions import plot_correlation_matrix
from functions.functions import return_positive_negative
from functions.functions import BuySellStocks

# Importar la clase encargada de construir el reporte
from main import ReportFinancial