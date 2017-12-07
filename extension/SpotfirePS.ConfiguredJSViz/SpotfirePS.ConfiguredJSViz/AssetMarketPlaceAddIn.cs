using System;
using Spotfire.Dxp.Application.Extension;
using SpotfirePS.Framework.JSVisualization;

namespace Spotfire.AssetMarketPlace
{
    public class AssetMarketPlaceAddIn : AddIn
    {
        protected override void RegisterVisuals(VisualRegistrar registrar)
        {
            base.RegisterVisuals(registrar);
            try
            {
                registrar.Register(new JSVisualizationPlotFactory());
            }
            catch (Exception)
            {
                ;
                //throw;
            }
            registrar.Register(new AssetMarketPlaceFactory());
        }
    }
}
