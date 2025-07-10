CONFIG = {
    "intensity_thresh": -1.0,
    "max_nodes": 100,
    "node_tracking_dist_thresh": 8,      # for Hungarian matching and lost node recovery
    "spatial_edge_thresh": 100,          # squared distance for edge creation
    "lost_ttl": 20,                      # frames to keep lost nodes
    "resize_shape": (256, 256),            # image resize shape;  Increased from (64, 64)
    # Add other parameters as needed
}