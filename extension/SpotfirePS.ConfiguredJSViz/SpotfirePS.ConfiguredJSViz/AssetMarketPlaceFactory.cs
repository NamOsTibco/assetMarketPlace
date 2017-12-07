using System.IO;
using System.Linq;
using System.Reflection;
using Spotfire.Dxp.Application;
using Spotfire.Dxp.Application.Extension;
using SpotfirePS.Framework.JSVisualization;
using SpotfirePS.Framework.JSVisualization.Core;
using Spotfire.AssetMarketPlace.Properties;


namespace Spotfire.AssetMarketPlace
{
    internal sealed class AssetMarketPlaceFactory : ConfiguredVisualFactory<JSVisualizationModel>
    {

        public AssetMarketPlaceFactory() :
            base(
            JSVisualizationIdentifiers.JSVisualization,
            AssetMarketPlaceTypeIdentifier.AssetMarketPlaceIdentifier,
            VisualCategory.Visualization,
            Resources.MarketPlaceIcon,
            null)
        {
            
        }

        protected override void AutoConfigureCore(JSVisualizationModel visual)
        {   
            base.AutoConfigureCore(visual);
            var doc = visual.Context.GetAncestor<Document>();

            // Add the files;
            string baseUrl = @"https://s3-eu-west-1.amazonaws.com/asset-market-place-sources";
            var cr = doc.CustomNodes.AddNewIfNeeded<ContentRepository>();

            string name = @"JQuery 3.2.1";
            string url = baseUrl + @"/externalLibs/jquery/jquery-3.2.1.min.js";
            var urlReference = new UrlReference(name, url, null, ContentType.JS, false);
            cr[name] = urlReference;
            visual.UrlInclusions.Add(name);

            name = @"JSVIZ";
            url = baseUrl + @"/externalLibs/jsviz/lib/JSViz/JSViz.js";
            urlReference = new UrlReference(name, url, null, ContentType.JS, false);
            cr[name] = urlReference;
            visual.UrlInclusions.Add(name);

            name = @"JVizIntrospectionJS";
            url = baseUrl + @"/externalLibs/jsviz/lib/JSViz/Introspection.js";
            urlReference = new UrlReference(name, url, null, ContentType.JS, false);
            cr[name] = urlReference;
            visual.UrlInclusions.Add(name);

            name = @"Namos Rotating Card CSS";
            url = baseUrl + @"/customLibs/NamOsMarketPlace/namos-rotating-card.css";
            urlReference = new UrlReference(name, url, null, ContentType.CSS, false);
            cr[name] = urlReference;
            visual.UrlInclusions.Add(name);

            name = @"Bootstrap";
            url = baseUrl + @"/externalLibs/bootstrap/bootstrap.min.js";
            urlReference = new UrlReference(name, url, null, ContentType.JS, false);
            cr[name] = urlReference;
            visual.UrlInclusions.Add(name);

            name = @"Angular";
            url = baseUrl + @"/externalLibs/angular/1.1.1/angular.min.js";
            urlReference = new UrlReference(name, url, null, ContentType.JS, false);
            cr[name] = urlReference;
            visual.UrlInclusions.Add(name);

            name = @"Asset Controller";
            url = baseUrl + @"/customLibs/NamOsMarketPlace/assetController.js";
            urlReference = new UrlReference(name, url, null, ContentType.JS, false);
            cr[name] = urlReference;
            visual.UrlInclusions.Add(name);

            name = @"namosMarketPlace";
            url = baseUrl + @"/customLibs/NamOsMarketPlace/namosMarketPlace.js";
            urlReference = new UrlReference(name, url, null, ContentType.JS, false);
            cr[name] = urlReference;
            visual.UrlInclusions.Add(name);

            name = @"NamosMarketPlace HTML";
            url = baseUrl + @"/customLibs/NamOsMarketPlace/namos-rotating-card.html";
            urlReference = new UrlReference(name, url, null, ContentType.HTML, false);
            cr[name] = urlReference;
            visual.UrlInclusions.Add(name);

            name = @"Bootstrap 3 CSS";
            url = baseUrl + @"/externalLibs/bootstrap/v3.0.2/bootstrap.css";
            urlReference = new UrlReference(name, url, null, ContentType.CSS, false);
            cr[name] = urlReference;
            visual.UrlInclusions.Add(name);

            name = @"Bootstrap CSS";
            url = baseUrl + @"/bootstrap/bootstrap.css";
            urlReference = new UrlReference(name, url, null, ContentType.CSS, false);
            cr[name] = urlReference;

            name = @"Platform";
            url = baseUrl + @"/externalLibs/platform.js-master/platform.js";
            urlReference = new UrlReference(name, url, null, ContentType.JS, false);
            cr[name] = urlReference;

            visual.Title = "AssetMarketPlace";
            visual.Visual.ShowTitle = true;
            visual.LegendVisible = false;

            visual.AutoConfigure();

        }


        /// <summary>
        /// Gets the embedded resource specified by the name.
        /// </summary>
        /// <param name="resourceName">Name of the resource.</param>
        /// <returns>
        /// The resource bytes, or null.
        /// </returns>
        public static new byte[] GetEmbeddedResource(string resourceName)
        {
            if (string.IsNullOrEmpty(resourceName))
            {
                return null;
            }

            var assembly = Assembly.GetCallingAssembly();

            var names = assembly.GetManifestResourceNames();
            if (!names.Contains(resourceName))
            {
                return null;
            }
            using (var stream = assembly.GetManifestResourceStream(resourceName))
            {
                if (stream != null)
                {
                    using (var ms = new MemoryStream())
                    {
                        CopyContent(stream, ms);
                        return ms.ToArray();
                    }
                }
            }

            return null;
        }

        internal static void CopyContent(Stream fromStream, Stream toStream)
        {

            byte[] buf = new byte[8 * 1024]; // Arbitrary buffer size.
            while (true)
            {
                int n = fromStream.Read(buf, 0, buf.Length);
                if (n <= 0)
                {
                    break;
                }

                toStream.Write(buf, 0, n);
            }
        }
    }
}
