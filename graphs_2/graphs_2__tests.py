#Wiernasiewicz_Wiktor_405029
import unittest
import graphs_2
import networkx as nx

class TestMinTrail(unittest.TestCase):
    def test_find_min_trail(self):

        g = nx.MultiDiGraph()
        g.add_weighted_edges_from([(1, 2, 0.5), (2, 3, 0.4), (2, 3, 0.3), (1, 3, 1.0)])
        v_start = 1
        v_end = 3
        min_trail_aktualny = graphs_2.find_min_trail(g, v_start, v_end)
        min_trail_oczekiwany = [graphs_2.TrailSegmentEntry(1, 2, 0, 0.5),graphs_2.TrailSegmentEntry(2, 3, 1, 0.3),]
        self.assertListEqual(min_trail_aktualny, min_trail_oczekiwany)
        total_weight = sum(w for (_, _, _, w) in min_trail_oczekiwany)
        self.assertEqual(total_weight, nx.dijkstra_path_length(g, v_start, v_end))

if __name__ == '__main__':
    unittest.main()
