using Spotfire.Dxp.Application.Extension;

namespace Spotfire.AssetMarketPlace
{
    public sealed class AssetMarketPlaceTypeIdentifier : CustomTypeIdentifiers
    {
        public static readonly CustomTypeIdentifier AssetMarketPlaceIdentifier =
            CreateTypeIdentifier("AssetMarketPlace", 
                                "Asset Marketplace", 
                                "Spotfire Asset Marketplace");
    }
}
