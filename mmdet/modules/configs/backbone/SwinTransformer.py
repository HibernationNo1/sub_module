pretrained ='https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_tiny_patch4_window7_224.pth'


backbone=dict(
    type='SwinTransformer',
    embed_dims=96,
    depths=[2, 2, 6, 2],
    num_heads=[3, 6, 12, 24],
    window_size=9,
    mlp_ratio=3,
    qkv_bias=True,
    qk_scale=None,
    drop_rate=0.,
    attn_drop_rate=0.3,
    drop_path_rate=0.0,
    patch_norm=True,
    out_indices=(0, 1, 2, 3),
    with_cp=False,
    convert_weights=True,	# add backbone name before layer name when run weight initalization
                            # if True : patch_embed.projection.weight >> backbone.patch_embed.projection.weight
    init_cfg=dict(type='Pretrained', checkpoint=pretrained))		 # fine tuning