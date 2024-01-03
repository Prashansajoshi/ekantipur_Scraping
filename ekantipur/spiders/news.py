import scrapy

class eKantipur(scrapy.Spider):
    name = "kantipur"
    start_urls = ['https://ekantipur.com/news']

    def parse(self, response):
        ekantipur_scraping = response.css('section')

        for ekantipur in ekantipur_scraping:
            date = ekantipur.css('#masthead div.mainContent a div.todays-date time::text').get()
            logo_image_url = ekantipur.css('#masthead .logo img::attr(src)').get()
            weather = ekantipur.css('#masthead .todays-weather .temp::text').get()

            yield {
                "source": "ekantipur",
                "type": "news",
                "data": {
                    "date": date,
                    "logo_image_url": logo_image_url,
                    "weather": weather,
                }
            }

        site_nav_section = response.css('#site_nav_section')
        for site_nav in site_nav_section:
            nav = site_nav_section.css('.mainContent .nav-bar ul li a::attr(href)').extract()
            yield {
                "source": "ekantipur",
                "type": "navigation",
                "data": {
                    "nav": nav
                }
            }

        main_contents = response.css('#nav-section')
        for main_content in main_contents:
            content = main_content.css('.title::text').extract()
            trending = main_content.css('#panelscroller ul li a::attr(href)').extract()
            yield {
                "source": "ekantipur",
                "type": "main_content",
                "data": {
                    "content": content,
                    "trending": trending
                }
            }

        mains = response.css('main')
        for main in mains:
            catname = mains.css('.row .catName::text').extract()
            article = mains.css('.listLayout .row h2 a::text').extract()
            author = mains.css('.listLayout .row .author a::text').extract()
            content_inside = mains.css('.listLayout .row p::text').extract()
            yield {
                "source": "ekantipur",
                "type": "main_section",
                "data": {
                    "catname": catname,
                    "article": article,
                    "author": author,
                    "content_inside": content_inside
                }
            }

        footers = response.css('footer')
        for footer in footers:
            footer_text = footers.css('.footer .wrap .row h2 span.footerCategoryText::text').extract()
            footer_content = footers.css('.footer .wrap .row ul.list-inline li a::text').extract()
            yield {
                "source": "ekantipur",
                "type": "footer",
                "data": {
                    "footer_text": footer_text,
                    "footer_content": footer_content
                }
            }

    


       
        

        
       
        


