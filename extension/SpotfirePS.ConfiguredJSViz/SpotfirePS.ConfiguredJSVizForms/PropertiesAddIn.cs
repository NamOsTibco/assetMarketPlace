using System;
using Spotfire.Dxp.Application.Extension;
using System.Windows.Forms;
using SpotfirePS.Framework.JSVisualization.Core;
using SpotfirePS.Framework.JSVisualizationForms.Forms;

namespace Spotfire.AssetMarketPlaceForms
{
    public class PropertiesAddIn : AddIn
    {
        protected override void RegisterViews(ViewRegistrar registrar)
        {
            base.RegisterViews(registrar);
            try
            {
                registrar.Register(typeof(Form), typeof(JSVisualizationModel), typeof(JSVisulizationPropertyDialog)); 
            }
            catch (Exception)
            {
                ;
                //throw;
            }
        }
    }
}
