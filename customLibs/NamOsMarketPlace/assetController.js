var hostName = "172.31.17.83";


var tciApiBaseUrl = "https://eu-west-1.integration.cloud.tibcoapps.com:443/sm5q2ml2hdharerbhmr6i2mawodtciri";
var liveAppsSandbox = "31";

//var hostName = "localhost";


function changeStyle (themeCssUrl) {
		
			console.log("***************************here");
			var res =  $('.card');
			
			//window.parent.$('head').append('<link rel="stylesheet" type="text/css" href="http://" + hostName+":8888/spotfireFramework/customLibs/NamOsMarketPlace/themes/NamOsNewTheme.css">');
			
			window.parent.$('head').append('<link rel="stylesheet" type="text/css" href="' + themeCssUrl + '">');
			
			var resStyle =  window.parent.$('style');
			console.log("****************SIZE BEFORE " + resStyle.size());
			window.parent.$('style').remove();
			
			console.log("***************************done");
		}



function assetController($scope, $http) {
	
		$scope.modifySearch = function (searchCat) {
			$scope.searchText = searchCat;
		};
	
		$scope.searchText = "";
		
		
		$scope.getNumber = function(num) {
			return new Array(num);   
		}
		
		$scope.ngExecute = function (asset) {
			console.log("***********************EXECUTE asset : " + JSON.stringify(asset));
			var implementationFileFullUrl = tciApiBaseUrl + "/getAssetFile?caseRef=" + asset.caseReference + "&sandBox="  + liveAppsSandbox  + "&fileName=" + asset.ImplementationFile;
			//alert(implementationFileFullUrl);
			
			if (asset.ImplementationType == "PYTHON") {
				console.log("EXECUTE PYTHON SCRIPT : " + implementationFileFullUrl);
				execScript(implementationFileFullUrl);
			} else if (asset.ImplementationType == "STYLE") {
				console.log("EXECUTE STYLE SCRIPT : " + implementationFileFullUrl);
				changeStyle(implementationFileFullUrl);
			}
			
			
			
			
		}
	
		$scope.assetCategories = [ "Template", "Theme" , "Visualization", "Script", "BPM", "LiveApps" ];
		
		$http({
			url: tciApiBaseUrl + "/getAssetDetails",
			method: "GET",
			mode: "cors"
		}).success(function (data, status, headers, config) {
			console.log("data " + data);
			$scope.assets= data;
			//$scope.apply();
			console.log("$scope.assets" + JSON.stringify($scope.assets));
		});
		
		/*$scope.assets = [{
						name : "Simple Page layout Template 1",
						description : "Simple Page layout Template 1",
						icon : "layout1.png",
						category : "Template",
						subcategory : "",
						tags : "",
						date : "10/10/2017",
						author : "NamOs",
						version : "1.0"	,
						imageDesc : "layout1.png",
						implementationType : "PYTHON",
						like : 1,
						implementationFile : "http://" + hostName+":8888/spotfireFramework/customLibs/ironPythonLib/templateLayout1.py"
					  },{
						name : "Simple Page layout Template 2",
						description : "Simple Page layout Template 2",
						icon : "layout2.png",
						category : "Template",
						subcategory : "",
						tags : "",
						date : "10/10/2017",
						author : "NamOs",
						version : "1.0"	,
						imageDesc : "layout2.png",
						like : 1,
						implementationType : "PYTHON",
						implementationFile : "http://" + hostName+":8888/spotfireFramework/customLibs/ironPythonLib/templateLayout2.py"
					  },{
						name : "Simple Page layout Template 3",
						description : "Simple Page layout Template 3",
						icon : "layout3.png",
						category : "Template",
						subcategory : "",
						tags : "",
						date : "10/10/2017",
						author : "NamOs",
						version : "1.0"	,
						imageDesc : "layout3.png",
						like : 1,
						implementationType : "PYTHON",
						implementationFile : "http://" + hostName+":8888/spotfireFramework/customLibs/ironPythonLib/templateLayout3.py"
					  },{
						name : "Simple Page layout Template 4",
						description : "Simple Page layout Template 4",
						icon : "layout4.png",
						category : "Template",
						subcategory : "",
						tags : "",
						date : "10/10/2017",
						author : "NamOs",
						version : "1.0"	,
						imageDesc : "layout4.png",
						like : 1,
						implementationType : "PYTHON",
						implementationFile : "http://" + hostName+":8888/spotfireFramework/customLibs/ironPythonLib/templateLayout4.py"
					  },{
						name : "Simple Application Template",
						description : "Simple Application Template",
						icon : "missing.png",
						category : "Template",
						subcategory : "",
						tags : "",
						date : "10/10/2017",
						author : "NamOs",
						version : "1.0"	,
						imageDesc : "sampleApplication.png",
						like : 3,
						implementationType : "PYTHON",
						implementationFile : "http://" + hostName+":8888/spotfireFramework/customLibs/ironPythonLib/createApplication.py"
					  },{
						name : "Overview Page on Customer Data",
						description : "Overview Page on Customer Data",
						icon : "missing.png",
						category : "Template",
						subcategory : "",
						tags : "",
						date : "10/10/2017",
						author : "NamOs",
						version : "1.0"	,
						imageDesc : "sampleApplication.png",
						like : 3,
						implementationType : "PYTHON",
						implementationFile : "http://" + hostName+":8888/spotfireFramework/customLibs/ironPythonLib/createOveriewCFO.py"
					  }
					  ,{
						name : "Dark Blue paperscreen (Dark) ",
						description : "A simple Dark Blue paperscreen (Dark) Theme",
						icon : "dark_blue_piece_of_paper_icon.jpg",
						category : "Theme",
						subcategory : "",
						tags : "",
						date : "10/10/2017",
						author : "NamOs",
						version : "1.0"	,
						imageDesc : "missing.png",
						like : 3,
						implementationType : "STYLE",
						implementationFile : "http://" + hostName+":8888/spotfireFramework/customLibs/NamOsMarketPlace/themes/DarkBluePaper-Dark.css"
					  },{
						name : "Dark Blue paperscreen (Light) ",
						description : "A simple Dark Blue paperscreen (Light) Theme",
						icon : "dark_blue_light_piece_of_paper_icon.jpg",
						category : "Theme",
						subcategory : "",
						tags : "",
						date : "10/10/2017",
						author : "NamOs",
						version : "1.0"	,
						imageDesc : "missing.png",
						like : 3,
						implementationType : "STYLE",
						implementationFile : "http://" + hostName+":8888/spotfireFramework/customLibs/NamOsMarketPlace/themes/DarkBluePaper-Light.css"
					  }
					  ,{
						name : "Gray paperscreen ",
						description : "A simple Gray paperscreen Theme",
						icon : "gray_paper_screen_shot.png",
						category : "Theme",
						subcategory : "",
						tags : "",
						date : "10/10/2017",
						author : "NamOs",
						version : "1.0"	,
						imageDesc : "missing.png",
						like : 3,
						implementationType : "STYLE",
						implementationFile : "http://" + hostName+":8888/spotfireFramework/customLibs/NamOsMarketPlace/themes/GrayPaper.css"
					  },{
						name : "Gray and gold tile",
						description : "A simple gray and gold tilen Theme",
						icon : "gray_and_gold_tile.png",
						category : "Theme",
						subcategory : "",
						tags : "",
						date : "10/10/2017",
						author : "NamOs",
						version : "1.0"	,
						imageDesc : "missing.png",
						like : 2,
						implementationType : "STYLE",
						implementationFile : "http://" + hostName+":8888/spotfireFramework/customLibs/NamOsMarketPlace/themes/GrayGoldTile.css"
					  },{
						name : "Light blue tiles",
						description : "A simple light blue Theme",
						icon : "light_blue_tiles_theme.jpg",
						category : "Theme",
						subcategory : "",
						tags : "",
						date : "10/10/2017",
						author : "NamOs",
						version : "1.0"	,
						imageDesc : "missing.png",
						like : 1,
						implementationType : "STYLE",
						implementationFile : "http://" + hostName+":8888/spotfireFramework/customLibs/NamOsMarketPlace/themes/LightBlueTile.css"
					  },{
						name : "Gray CFO",
						description : "A simple gray Theme",
						icon : "missing.png",
						category : "Theme",
						subcategory : "",
						tags : "",
						date : "10/10/2017",
						author : "NamOs",
						version : "1.0"	,
						imageDesc : "missing.png",
						like : 1,
						implementationType : "STYLE",
						implementationFile : "http://" + hostName+":8888/spotfireFramework/customLibs/NamOsMarketPlace/themes/GrayCFO.css"
					  },{
						name : "Graph Viz",
						description : "A JSViz Visualisation that produce Grapz",
						icon : "graph.png",
						category : "Visualization",
						subcategory : "Custom Visualization",
						tags : "",
						date : "10/10/2017",
						author : "NamOs",
						version : "1.0",
						imageDesc : "graphDesc.png",
						like : 3,
						implementationType : "PYTHON",
						implementationFile : "http://" + hostName+":8888/spotfireFramework/customLibs/ironPythonLib/createVisTimeline.py"
						
					  },
{
						name : "Timeline Viz",
						description : "A JSViz Visualisation that show a timeline",
						icon : "timeline.png",
						category : "Visualization",
						subcategory : "Custom Visualization",
						tags : "",
						date : "10/10/2017",
						author : "NamOs",
						version : "1.0",
						imageDesc : "visTimelineDesc.png",
						like : 2,
						implementationType : "PYTHON",
						implementationFile : "http://" + hostName+":8888/spotfireFramework/customLibs/ironPythonLib/createVisTimeline.py"
						
					  },{
						name : "Create Folder",
						description : "A Iron Python script that creates a folder",
						icon : "createFolder.png",
						category : "Script",
						subcategory : "Misc",
						tags : "",
						date : "10/10/2017",
						author : "Heleen Snelting",
						version : "1.0",
						imageDesc : "visTimelineDesc.png",
						like : 2,
						implementationType : "PYTHON",
						implementationFile : "http://" + hostName+":8888/spotfireFramework/customLibs/ironPythonLib/createPage.py"
						
					  },{
						name : "Work Items performance",
						description : "Work Items performance Page",
						icon : "missing.png",
						category : "BPM",
						subcategory : "",
						tags : "",
						date : "10/10/2017",
						author : "NamOs",
						version : "1.0"	,
						imageDesc : "missing.png",
						like : 2,
						implementationType : "PYTHON",
						implementationFile : "http://" + hostName+":8888/spotfireFramework/customLibs/ironPythonLib/createPage.py"
					  },{
						name : "Process Performance",
						description : "Process Performance",
						icon : "missing.png",
						category : "BPM",
						subcategory : "",
						tags : "",
						date : "10/10/2017",
						author : "NamOs",
						version : "1.0"	,
						imageDesc : "missing.png",
						like : 1,
						implementationType : "PYTHON",
						implementationFile : "http://" + hostName+":8888/spotfireFramework/customLibs/ironPythonLib/createPage.py"
					  },{
						name : "List Apps",
						description : "Simple LiveApps dashboard that list Apps",
						icon : "missing.png",
						category : "LiveApps",
						subcategory : "",
						tags : "",
						date : "10/10/2017",
						author : "NamOs",
						version : "1.0"	,
						imageDesc : "missing.png",
						like : 1,
						implementationType : "PYTHON",
						implementationFile : "http://" + hostName+":8888/spotfireFramework/customLibs/ironPythonLib/createPage.py"
					  }];*/
}
	
