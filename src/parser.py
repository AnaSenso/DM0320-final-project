from argparse import ArgumentParser

def parse():
    parser = ArgumentParser(description="Get Factorial anlysis report form a B5 personality test.")
    parser.add_argument("--ds", help="Introduce sample dataset name", type=str, default='IPIP_20_test')
    parser.add_argument("--inf", help="Introduce info data set name", type=str, default='IPIP_20_desc_item')
    parser.add_argument("--an", help="Seelect the type of analysis you want: Item (it) or Dimension (dm).", type=str, default='dm')
    return parser.parse_args()