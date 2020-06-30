import sys
import json


class JsonToCsv:
    file_name = sys.argv[1]
    file = open(file_name, "r")
    print("Reading File: [", file_name, "]")
    data = json.load(file)
    file.close()
    name = str(data['dataset'][0]['name'])
    data_stats = data['dataset'][0]['stats'][0]
    total_nodes = str(data_stats['total_nodes'])
    mean_depth_tree = str(data_stats['mean_depth_tree'])
    sd_depth_per_tree = str(data_stats['sd_depth_per_tree'])
    mean_nodes_per_tree = str(data_stats['mean_nodes_per_tree'])
    sd_nodes_per_tree = str(data_stats['sd_nodes_per_tree'])
    std_error_nodes_per_tree = str(data_stats['std_error_nodes_per_tree'])
    std_error_depth_per_tree = str(data_stats['std_error_depth_per_tree'])

    linea = name + ',' + total_nodes + ',' + mean_depth_tree + ',' + \
            sd_depth_per_tree + ',' + mean_nodes_per_tree + ',' + sd_nodes_per_tree + ',' + \
            std_error_nodes_per_tree + ',' + std_error_depth_per_tree
    f_path = '../csvresults/stats_' + name + '.csv'
    with open(f_path, 'w+') as file:
        file.writelines("name,total_nodes,mean_depth_tree,sd_depth_per_tree,mean_nodes_per_tree,sd_nodes_per_tree,"
                        "std_error_nodes_per_tree,std_error_depth_per_tree\n")
        file.writelines("%s\n" % linea)
        file.close()
